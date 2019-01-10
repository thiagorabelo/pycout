

# http://www.cplusplus.com/reference/iomanip/setfill/
def setfill(fill):
    def set_fill(stream):
        stream.fill(fill)
        return stream

    return set_fill


# http://www.cplusplus.com/reference/iomanip/setw/
def setw(width):
    def set_w(stream):
        stream.width(width)
        return stream

    return set_w


# TODO: implement std::fixed? http://www.cplusplus.com/reference/ios/fixed/
# http://www.cplusplus.com/reference/iomanip/setprecision/
def setprecision(prec):
    def set_precision(stream):
        stream.precision(prec)
        return stream

    return set_precision


# TODO: https://en.cppreference.com/w/cpp/io/manip/quoted
def quoted(string, delim='"', escape='\\'):
    raise NotImplementedError("Not yet implemented.")


# TODO: http://www.cplusplus.com/reference/iomanip/
# TODO: http://www.cplusplus.com/reference/ios/basic_ios/
