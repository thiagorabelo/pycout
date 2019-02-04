import abc
from typing import Text, Any

class BaseHandler(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def handle(self, value: Any) -> Text:
        pass


class DecHandler(BaseHandler):
    def handle(self, value: int) -> Text:
        return '%d' % value


class HexHandler(BaseHandler):
    def __init__(self, prefix: bool = False):
        self._prefix = prefix

    def handle(self, value: int) -> Text:
        if not self._prefix:
            if value >= 0:
                return hex(value)[2:]
            return f'-{hex(value)[3:]}'

        return hex(value)
