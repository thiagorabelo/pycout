
"""
Módulo que contém uma classe que simula a classe padrão ostream do C++
"""


import abc
import numbers

from sys import stdout


class OSManipulator(metaclass=abc.ABCMeta):  # pylint: disable=too-few-public-methods,
    @abc.abstractmethod                      #                 useless-object-inheritance
    def to_string(self, obj):
        pass


class DefaultOSManipulator(OSManipulator):  # pylint: disable=too-few-public-methods
    def to_string(self, obj):
        return '%s' % obj


class PrecicionManip(OSManipulator):  # pylint: disable=too-few-public-methods

    def __init__(self, prec):
        self.prec = prec

    def to_string(self, obj):
        if not isinstance(obj, numbers.Integral) and isinstance(obj, numbers.Real):
            # TODO: Eu sei que issa não é a forma certa. Ajeitar!
            # TODO: Implementacao do fixed depende de ajeitar essa funcionalidade.
            sformat = '%%.%df' % self.prec
            return sformat % obj
        return super(PrecicionManip, self).to_string(obj)

    # TODO: http://www.cplusplus.com/reference/ios/ios_base/precision/
    # TODO: implement std::fixed? http://www.cplusplus.com/reference/ios/fixed/
    def precision(self, prec=None):
        old = self.prec

        if prec:
            self.prec = prec

        return old


class FillManipulator(DefaultOSManipulator):  # pylint: disable=too-few-public-methods

    width_ = 0
    fill_ = ' '

    def to_string(self, obj):
        obj = super(FillManipulator, self).to_string(obj)

        if not self.width_:
            return obj

        try:
            idx = obj.index('\n')
            size = self.width_ - idx

            if idx == 0:
                return obj

        except ValueError:
            size = self.width_ - len(obj)

        out = (self.fill_ * size) + obj

        self.width_ = 0
        self.fill_ = ' '

        return out

    def width(self, width=None):
        old = self.width_

        if width:
            self.width_ = width

        return old

    def fill(self, fill=None):
        old = self.fill_

        if fill:
            self.fill_ = fill

        return old


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


# TODO: http://www.cplusplus.com/reference/iomanip/setfill/
def setfill(fill):
    def set_fill(stream):
        stream.fill(fill)
        return stream

    return set_fill


# TODO: http://www.cplusplus.com/reference/iomanip/setw/
def setw(width):
    def set_w(stream):
        stream.width(width)
        return stream

    return set_w


# TODO: http://www.cplusplus.com/reference/iomanip/setprecision/
# TODO: implement std::fixed? http://www.cplusplus.com/reference/ios/fixed/
def setprecision(prec):
    def set_precision(stream):
        stream.precision(prec)
        return stream

    return set_precision


# TODO: http://www.cplusplus.com/reference/iomanip/
# TODO: http://www.cplusplus.com/reference/ios/basic_ios/


if __name__ == '__main__':
    cout = OStream()  # pylint: disable=invalid-name

    # import time

    # pylint: disable=pointless-statement
    # pylint: disable=expression-not-assigned
    cout << "Olá mundo" \
         << " cruel! " \
         << 100.123 \
         << setprecision(2) << "\n" \
         << "depois do precision\n" \
         << 100.1234 \
         << " depois do número" \
         << endl \
         << "Hello World\n" \
         << setfill('*') \
         << setw(5) \
         << "a\nb" \
         << endl


    # time.sleep(3)
