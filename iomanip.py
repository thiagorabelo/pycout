from typing import Text, Callable

from ostream import OStream

# http://www.cplusplus.com/reference/iomanip/setfill/
def setfill(fill: Text) -> Callable[[OStream], OStream]:
    def set_fill(stream: OStream):
        stream.fill(fill)
        return stream

    return set_fill


# http://www.cplusplus.com/reference/iomanip/setw/
def setw(width: int):
    def set_w(stream) -> Callable[[OStream], OStream]:
        stream.width(width)
        return stream

    return set_w


# TODO: implement std::fixed? http://www.cplusplus.com/reference/ios/fixed/
# http://www.cplusplus.com/reference/iomanip/setprecision/
def setprecision(prec):
    def set_precision(stream) -> Callable[[OStream], OStream]:
        stream.precision(prec)
        return stream

    return set_precision


# TODO: https://en.cppreference.com/w/cpp/io/manip/quoted
def quoted(string, delim='"', escape='\\'):
    raise NotImplementedError("Not yet implemented.")


# TODO: http://www.cplusplus.com/reference/iomanip/
# TODO: http://www.cplusplus.com/reference/ios/basic_ios/
