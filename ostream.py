
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
        return self._output.write(stream)

    def flush(self):
        return self._output.flush()

def endl(stream):
    stream.write('\n')
    stream.flush()
    return stream


if __name__ == '__main__':
    cout = OStream()  # pylint: disable=invalid-name

    # import time

    # pylint: disable=pointless-statement
    cout << "Olá mundo" \
         << " cruel! " \
         << 100 \
         << endl

    # time.sleep(3)
