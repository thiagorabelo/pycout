
"""
Módulo que contém uma classe que simula a classe padrão ostream do C++
"""

import numbers
from sys import stdout

from .base_ostream import PrecicionManip, FillManipulator


class OStream(PrecicionManip, FillManipulator):  # pylint: disable=useless-object-inheritance

    def __init__(self, output=stdout):
        self._output = output
        super(OStream, self).__init__(6)

    def _to_string(self, obj):
        return '%s' % obj

    def _proccess(self, obj):
        if isinstance(obj, numbers.Real) and not isinstance(obj, numbers.Integral):
            obj = self._proccess_numbers(obj)

        if self.width_:
            return self._fill_str(self._to_string(obj))

        return self._to_string(obj)

    def __lshift__(self, stream):
        return self.write(stream)

    def write(self, stream):
        if callable(stream):
            return stream(self)
        self._output.write(self._proccess(stream))
        return self

    def put(self, char):
        self._output.write(self._proccess(char)[0])
        return self

    def flush(self):
        return self._output.flush()


def endl(stream):
    stream << '\n'  # pylint: disable=pointless-statement
    stream.flush()
    return stream


def ends(stream):
    stream.write('\0')
    return stream


def flush(stream):
    stream.flush()
    return stream
