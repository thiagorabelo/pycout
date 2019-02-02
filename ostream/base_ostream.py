import abc
from typing import Union, Text, Any, Type

from .precisions import PrecisionHandler, DefaultPrecision


class Manip(metaclass=abc.ABCMeta):  # pylint: disable=too-few-public-methods
    @abc.abstractmethod
    def _proccess(self, value: Any) -> Text:
        pass

    @staticmethod
    def _to_string(value: Any) -> Text:
        return '%s' % value


class PrecicionManip(Manip):  # pylint: disable=too-few-public-methods

    _prec_handler_class: Type[PrecisionHandler] = DefaultPrecision
    _prec_handler: PrecisionHandler = _prec_handler_class(6)

    def _proccess(self, value: float) -> Text:
        return self._prec_handler.handle(value)

    # TODO: implement std::{fixed, scientific, hexfloat, defaultfloat}?
    #       https://en.cppreference.com/w/cpp/io/manip/fixed
    #       http://www.cplusplus.com/reference/ios/fixed/
    def precision(self, prec: Union[int, None] = None) -> int:
        old = self._prec_handler

        if prec is not None:
            self._prec_handler = self._prec_handler_class(prec)

        return old.precision

    def _set_prec_handler(self, handler_class: Type[PrecisionHandler]) -> None:
        prec = self._prec_handler.precision
        self._prec_handler_class = handler_class
        self.precision(prec)


# TODO: Fill deverá herdar de Quoted, e a chamada ao processamento
#       de Quoted deverá ser feito primeiro, através da chamada ao
#       método da classe base.
class FillManipulator(Manip):  # pylint: disable=too-few-public-methods

    width_: int = 0
    fill_: Text = ' '

    def _proccess(self, value: Text):
        if self.width_:
            return self._fill_str(self._to_string(value))

        return self._to_string(value)

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
