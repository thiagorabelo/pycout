import abc
import math
import numbers
from typing import Union, Text, Any


class Manip(metaclass=abc.ABCMeta):  # pylint: disable=too-few-public-methods
    @abc.abstractmethod
    def _proccess(self, value: Any) -> Text:
        pass


class PrecisionHandle(metaclass=abc.ABCMeta):
    def __init__(self, precision=6):
        if precision < 1:
            raise ValueError('precision should be bigger than 0')
        self._precision = precision

    @property
    def precision(self):
        return self._precision

    @abc.abstractmethod
    def handle(self, value: float) -> Text:
        pass


class Scientific(PrecisionHandle):

    @classmethod
    def _round_half_up(cls, number, decimals=0):
        multiplier = 10 ** decimals
        return math.floor(number*multiplier + 0.5) / multiplier

    @classmethod
    def _round_half_away_from_zero(cls, number, decimals=0):
        rounded_abs = cls._round_half_up(abs(number), decimals)
        return math.copysign(rounded_abs, number)

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

    def handle(self, value: float) -> Text:
        str_value = '%f' % abs(value)
        signal = '-' if value < 0.0 else ''

        if 0.0 < abs(value) < 1.0:
            integer, decimal = str_value.split('.')
            decimal = self._strip_right(decimal)
            return f'{signal}{integer}.{decimal}'

        integer, decimal = self._split(str_value)

        if self._precision < len(integer) + len(decimal):
            while decimal:
                if self._precision >= len(integer) + len(decimal):
                    return f'{signal}{integer}.{decimal}'
                decimal = self._strip_right(decimal[:-1])

            if self._precision >= len(integer):
                return str(integer)

            decimal = integer[1:]
            integer = integer[0]
            base = len(decimal)

            while decimal and self._precision < len(integer) + len(decimal):
                decimal = decimal[:-1]

            if decimal:
                return f'{signal}{integer}.{decimal}e+{base}'
            return f'{signal}{integer}e+{base}'

        return f'{signal}{integer}.{decimal}'


class PrecicionManip(Manip):  # pylint: disable=too-few-public-methods

    """
    cout << "Lá vai\n"
         << f << "\n"
         << setprecision(6) << f << "\n"
         << setprecision(5) << f << "\n "
         << setprecision(4) << f << "\n "
         << setprecision(3) << f << "\n "
         << setprecision(2) << f << "\n "
         << setprecision(1) << f << "\n";

    # Ouput:

    Lá vai
    123.456
    123.456
    123.46
    123.5
    123
    1.2e+02
    1e+02

    #############

    # Com fixed

    cout << "Lá vai\n"
         << f << "\n"
         << fixed
         << setprecision(6) << f << "\n"
         << setprecision(5) << f << "\n"
         << setprecision(4) << f << "\n"
         << setprecision(3) << f << "\n"
         << setprecision(2) << f << "\n"
         << setprecision(1) << f << "\n";

    Lá vai
    123.456
    123.456001
    123.45600
    123.4560
    123.456
    123.46
    123.5
    """

    @abc.abstractmethod
    def _proccess(self, value):
        pass

    prec: int = 6

    def _proccess_numbers(self, value: float) -> Text:
        if not isinstance(value, numbers.Integral) and isinstance(value, numbers.Real):
            # TODO: Eu sei que issa não é a forma certa. Ajeitar!
            # TODO: Implementacao do 'fixed' e  depende de ajeitar essa funcionalidade.
            sformat = '%%.%df' % self.prec
            return sformat % value
        return '%s' % value

    # TODO: implement std::{fixed, scientific, hexfloat, defaultfloat}?
    #       https://en.cppreference.com/w/cpp/io/manip/fixed
    def precision(self, prec: Union[int, None] = None) -> int:
        old = self.prec

        if prec:
            self.prec = prec

        return old


class FillManipulator(Manip):  # pylint: disable=too-few-public-methods

    width_: int = 0
    fill_: Text = ' '

    @abc.abstractmethod
    def _proccess(self, value):
        pass

    def _fill_str(self, value: Text) -> Text:
        size = self.width_ - len(value)

        if not self.width_ or size <= 0:
            return value

        out = (self.fill_ * size) + value

        self.width_ = 0
        self.fill_ = ' '

        return out

    def width(self, width: Union[int, None] = None) -> int:
        old = self.width_

        if width:
            self.width_ = width

        return old

    def fill(self, fill: Union[Text, None] = None) -> Text:
        old = self.fill_

        if fill:
            self.fill_ = fill

        return old


if __name__ == '__main__':
    print(Scientific(6).handle(1.0))
    print(Scientific(6).handle(123.456))
    print(Scientific(5).handle(123.456))
    print(Scientific(4).handle(123.456))
    print(Scientific(3).handle(123.456))
    print(Scientific(2).handle(123.456))
    print(Scientific(1).handle(123.456))
