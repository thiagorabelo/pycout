
"""
Módulo que contém uma classe que simula a classe padrão ostream do C++
"""

import numbers
from sys import stdout
from typing import Union, Callable, IO, Text, Any

from .base_ostream import PrecicionManip, FillManipulator


class OStream(PrecicionManip, FillManipulator):  # pylint: disable=useless-object-inheritance

    def __init__(self, output_stream: IO[Text] = stdout) -> None:
        self._stream = output_stream

    def _to_string(self, value: Any) -> Text:
        return '%s' % value

    def _proccess(self, value: Text) -> Text:
        if isinstance(value, numbers.Real) and not isinstance(value, numbers.Integral):
            value = self._proccess_numbers(value)

        # TODO: quoted deve vir aqui.

        if self.width_:
            return self._fill_str(self._to_string(value))

        return self._to_string(value)

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


def endl(stream: OStream) -> OStream:
    stream << '\n'  # pylint: disable=pointless-statement
    stream.flush()
    return stream


def ends(stream: OStream) -> OStream:
    stream.write('\0')
    return stream


def flush(stream: OStream) -> OStream:
    stream.flush()
    return stream
