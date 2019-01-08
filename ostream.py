
"""
Módulo que contém uma classe que simula a classe padrão ostream do C++
"""


from sys import stdout


class OStream(object):  # pylint: disable=useless-object-inheritance

    def __init__(self, output=stdout):
        self._output = output

    def _to_string(self, stream):  # pylint: disable=no-self-use
        return '%s' % stream

    def __lshift__(self, stream):
        if callable(stream):
            return stream(self)
        self._output.write(self._to_string(stream))
        return self

    def write(self, stream):
        self._output.write(stream)
        return self

    def put(self, char):
        self._output.write(self._to_string(char)[0])
        return self

    def flush(self):
        return self._output.flush()

    # TODO: http://www.cplusplus.com/reference/ios/ios_base/precision/
    def precision(self, prec=None):
        # retornar a precisão anterior
        raise NotImplementedError("Not yet implemented.")

    # TODO: http://www.cplusplus.com/reference/ios/ios_base/width/
    def width(self, width_=None):
        # retorna o width anterior
        raise NotImplementedError("Not yet implemented.")

    # TODO: http://www.cplusplus.com/reference/ios/ios/fill/
    def fill(self, char=None):
        # retorna o fill anterior
        raise NotImplementedError("Not yet implemented.")


def endl(stream):
    stream.write('\n')
    stream.flush()
    return stream


# TODO: http://www.cplusplus.com/reference/iomanip/setfill/
def setfill(stream):
    raise NotImplementedError("Not yet implemented.")


# TODO: http://www.cplusplus.com/reference/iomanip/setprecision/
# TODO: implement std::fixed?
def setprecision(stream):
    raise NotImplementedError("Not yet implemented.")


# TODO: http://www.cplusplus.com/reference/iomanip/setw/
def setw(stream):
    raise NotImplementedError("Not yet implemented.")


# TODO: http://www.cplusplus.com/reference/iomanip/


if __name__ == '__main__':
    cout = OStream()  # pylint: disable=invalid-name

    # import time

    # pylint: disable=pointless-statement
    cout << "Olá mundo" \
         << " cruel! " \
         << 100 \
         << endl

    # time.sleep(3)
