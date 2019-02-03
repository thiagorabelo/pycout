import abc
import math
from typing import Text

class PrecisionHandler(metaclass=abc.ABCMeta):
    _min_precision: int = 1

    def __init__(self, precision=6):
        if precision < self._min_precision:
            raise ValueError(f'precision should be greater or equal than {self._min_precision}')
        self._precision = precision

    @abc.abstractmethod
    def handle(self, value: float) -> Text:
        pass

    @property
    def precision(self):
        return self._precision

    @classmethod
    def _remove_decimals_zeros(cls, value):
        try:
            value.index('.')
            size = 0
            for digit in reversed(value):
                if not digit == '0':
                    if digit == '.':
                        size -= 1
                    break
                size -= 1

            if size:
                return value[:size]
        except ValueError:
            pass

        return value

    @classmethod
    def _strip_right(cls, str_num, min_size=0, char='0'):
        while len(str_num) > min_size and str_num[-1] == char:
            str_num = str_num[:-1]
        return str_num

    @classmethod
    def _split(cls, value):
        try:
            integer, decimal = value.split('.')
            decimal = cls._strip_right(decimal, min_size=1)
        except ValueError:
            integer, decimal = value, '0'

        return integer, decimal


class DefaultPrecision(PrecisionHandler):

    # from: https://realpython.com/python-rounding/#rounding-half-up
    @classmethod
    def _round_half_up(cls, number, decimals=0):
        multiplier = 10 ** decimals
        return math.floor(number*multiplier + 0.5) / multiplier

    # from: https://realpython.com/python-rounding/#rounding-half-away-from-zero
    @classmethod
    def _round_half_away_from_zero(cls, number, decimals=0):
        rounded_abs = cls._round_half_up(abs(number), decimals)
        return math.copysign(rounded_abs, number)

    def handle(self, value: float) -> Text:
        str_value = '%f' % abs(value)

        integer, decimal = self._split(str_value)
        integer_size, decimal_size = len(integer), len(decimal)

        if integer_size <= self._precision:
            decimal_size = self._precision - integer_size
            str_format = '%%.%df' % decimal_size
            return self._remove_decimals_zeros(str_format % value)

        value = int(value) / (10.0 ** (integer_size - 1))
        str_value = self.handle(value)

        return '%se+%02d' % (self._remove_decimals_zeros(str_value), integer_size - 1)


class FixedPrecision(PrecisionHandler):
    _min_precision: int = 0

    def handle(self, value: float) -> Text:
        str_format = '%%.%df' % self._precision
        return str_format % value
