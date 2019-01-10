
"""
Módulo que contém uma classe que simula a classe padrão ostream do C++
"""


from sys import stdout

from .base_ostream import DefaultOSManipulator, PrecicionManip, FillManipulator


class OStream(PrecicionManip, FillManipulator):  # pylint: disable=useless-object-inheritance

    def __init__(self, output=stdout):
        self._output = output
        super(OStream, self).__init__(6)

    def __lshift__(self, stream):
        if callable(stream):
            return stream(self)
        self._output.write(self.to_string(stream))
        return self

    def write(self, stream):
        self._output.write(stream)
        return self

    def put(self, char):
        self._output.write(self.to_string(char)[0])
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
