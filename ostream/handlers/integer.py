import abc
import math
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
        value = hex(value)
        if not self._prefix:
            return value[2:]
        return value
