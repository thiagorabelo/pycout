import numbers
from typing import Union, Text


class PrecicionManip(object):  # pylint: disable=too-few-public-methods,useless-object-inheritance
    """
    cout << "Lá vai\n"
         << f << "\n"
         << setprecision(6) << f << "\n"
         << setprecision(5) << f << "\n"
         << setprecision(4) << f << "\n"
         << setprecision(3) << f << "\n"
         << setprecision(2) << f << "\n"
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


class FillManipulator(object):  # pylint: disable=too-few-public-methods,useless-object-inheritance

    width_: int = 0
    fill_: Text = ' '

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
