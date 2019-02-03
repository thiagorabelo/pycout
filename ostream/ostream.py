
"""
Módulo que contém uma classe que simula a classe padrão ostream do C++
"""

from sys import stdout
from typing import Union, Callable, IO, Text

from .base_ostream import PrecicionManip, FillManipulator, IntManip


class OStream(FillManipulator):  # pylint: disable=useless-object-inheritance

    # _type_dict = {
    #     float: PrecicionManip(),
    #     int: IntManip(),
    #     # bool, etc.
    # }

    def __init__(self, output_stream: IO[Text] = stdout) -> None:
        self._type_dict = {
            float: PrecicionManip(),
            int: IntManip(),
            # bool, etc.
        }

        self._stream = output_stream

    def _proccess(self, value: Text) -> Text:
        manip = self._type_dict.get(type(value))

        if manip:
            value = manip._proccess(value)  # pylint: disable=protected-access

        # TODO: quoted deve vir aqui.

        return super()._proccess(value)

    def __lshift__(self, value: Union[Text, int, float, bool,
                                      Callable[['OStream'], 'OStream']]) -> 'OStream':
        return self.write(value)

    def write(self, value: Union[Text, int, float, bool,
                                 Callable[['OStream'], 'OStream']]) -> 'OStream':
        if callable(value):
            return value(self)
        self._stream.write(self._proccess(value))
        return self

    def put(self, char: Text) -> 'OStream':
        self._stream.write(self._proccess(char)[0])
        return self

    def flush(self) -> None:
        self._stream.flush()

    def precision(self, prec: Union[int, None] = None) -> int:
        return self._type_dict[float].precision(prec)

    def _set_prec_handler(self, handler_class):
        # pylint: disable=protected-access
        self._type_dict[float]._set_prec_handler(handler_class)

    def _set_int_handler(self, handler):
        # pylint: disable=protected-access
        self._type_dict[int]._set_int_handler(handler)


def endl(stream: OStream) -> OStream:
    stream.write('\n')
    stream.flush()
    return stream


def ends(stream: OStream) -> OStream:
    stream.write('\0')
    return stream


def flush(stream: OStream) -> OStream:
    stream.flush()
    return stream
