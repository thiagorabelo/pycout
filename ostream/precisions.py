import abc
import math
from typing import Text

class PrecisionHandler(metaclass=abc.ABCMeta):
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


class Scientific(PrecisionHandler):
    """
    float f = 123.456;
    cout << "Lá vai = " << f << "\n"
         << setprecision(6) << f << "\n"
         << setprecision(5) << f << "\n "
         << setprecision(4) << f << "\n "
         << setprecision(3) << f << "\n "
         << setprecision(2) << f << "\n "
         << setprecision(1) << f << "\n";

    # Ouput:

    Lá vai = 123.456
    123.456
    123.46
    123.5
    123
    1.2e+02
    1e+02


    #############


    float f = 199.999;
    cout << "Lá vai = " << f << "\n"
         << setprecision(6) << f << "\n"
         << setprecision(5) << f << "\n "
         << setprecision(4) << f << "\n "
         << setprecision(3) << f << "\n "
         << setprecision(2) << f << "\n "
         << setprecision(1) << f << endl;

    # Output:

    Lá vai = 199.999
    199.999
    200
    200
    200
    2e+02
    2e+02


    #############


    # Com fixed
    float f = 123.456;
    cout << "Lá vai = " << f << "\n"
         << fixed
         << setprecision(6) << f << "\n"
         << setprecision(5) << f << "\n"
         << setprecision(4) << f << "\n"
         << setprecision(3) << f << "\n"
         << setprecision(2) << f << "\n"
         << setprecision(1) << f << "\n";

    Lá vai = 123.456
    123.456001
    123.45600
    123.4560
    123.456
    123.46
    123.5
    """


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

        integer, decimal = self._split(str_value)
        integer_size, decimal_size = len(integer), len(decimal)

        if integer_size <= self._precision:
            decimal_size = self._precision - integer_size
            str_format = '%%.%df' % decimal_size
            return str_format % value

        return str(value)


if __name__ == '__main__':
    print(Scientific(6).handle(123.456))
    print(Scientific(5).handle(123.456))
    print(Scientific(4).handle(123.456))
    print(Scientific(3).handle(123.456))
    print(Scientific(2).handle(123.456))
    print(Scientific(1).handle(123.456))
