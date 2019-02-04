import unittest

from ostream.handlers.integer import DecHandler, HexHandler


class TestIntHandler(unittest.TestCase):
    def test_dechandler(self):
        self.assertEqual('-608232', DecHandler().handle(-608232))
        self.assertEqual('110323', DecHandler().handle(110323))
        self.assertEqual('-166780', DecHandler().handle(-166780))
        self.assertEqual('191521', DecHandler().handle(191521))
        self.assertEqual('-72', DecHandler().handle(-72))
        self.assertEqual('48', DecHandler().handle(48))
        self.assertEqual('-36', DecHandler().handle(-36))
        self.assertEqual('2', DecHandler().handle(2))
        self.assertEqual('-6', DecHandler().handle(-6))
        self.assertEqual('-10', DecHandler().handle(-10))
        self.assertEqual('10', DecHandler().handle(10))
        self.assertEqual('0', DecHandler().handle(0))

    def test_hexhandler(self):
        self.assertEqual('-947e8', HexHandler().handle(-608232))
        self.assertEqual('1aef3', HexHandler().handle(110323))
        self.assertEqual('-28b7c', HexHandler().handle(-166780))
        self.assertEqual('2ec21', HexHandler().handle(191521))
        self.assertEqual('-48', HexHandler().handle(-72))
        self.assertEqual('30', HexHandler().handle(48))
        self.assertEqual('-24', HexHandler().handle(-36))
        self.assertEqual('2', HexHandler().handle(2))
        self.assertEqual('-6', HexHandler().handle(-6))
        self.assertEqual('-a', HexHandler().handle(-10))
        self.assertEqual('a', HexHandler().handle(10))
        self.assertEqual('0', HexHandler().handle(0))

    def test_hexhandler_prefix(self):
        self.assertEqual('-0x947e8', HexHandler(True).handle(-608232))
        self.assertEqual('0x1aef3', HexHandler(True).handle(110323))
        self.assertEqual('-0x28b7c', HexHandler(True).handle(-166780))
        self.assertEqual('0x2ec21', HexHandler(True).handle(191521))
        self.assertEqual('-0x48', HexHandler(True).handle(-72))
        self.assertEqual('0x30', HexHandler(True).handle(48))
        self.assertEqual('-0x24', HexHandler(True).handle(-36))
        self.assertEqual('0x2', HexHandler(True).handle(2))
        self.assertEqual('-0x6', HexHandler(True).handle(-6))
        self.assertEqual('-0xa', HexHandler(True).handle(-10))
        self.assertEqual('0xa', HexHandler(True).handle(10))
        self.assertEqual('0x0', HexHandler(True).handle(0))
