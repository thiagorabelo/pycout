import abc
import numbers


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
        size = self.width_ - len(obj)

        if not self.width_ or size <= 0:
            return obj

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
