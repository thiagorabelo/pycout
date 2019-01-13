import abc
import numbers
from typing import Union, Text, Any


class Manip(metaclass=abc.ABCMeta):  # pylint: disable=too-few-public-methods
    @abc.abstractmethod
    def _proccess(self, value: Any) -> Text:
        pass


class PrecicionManip(Manip):  # pylint: disable=too-few-public-methods

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
