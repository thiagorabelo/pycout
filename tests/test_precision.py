import unittest

from ostream.handlers import DefaultPrecision, FixedPrecision


class TestScentificPrecision(unittest.TestCase):

    def test_123_456(self):
        value = 123.456
        self.assertEqual("123.456", DefaultPrecision(6).handle(value))
        self.assertEqual("123.46", DefaultPrecision(5).handle(value))
        self.assertEqual("123.5", DefaultPrecision(4).handle(value))
        self.assertEqual("123", DefaultPrecision(3).handle(value))
        self.assertEqual("1.2e+02", DefaultPrecision(2).handle(value))
        self.assertEqual("1e+02", DefaultPrecision(1).handle(value))

    def test_approximation(self):
        value = 199.999
        self.assertEqual("199.999", DefaultPrecision(6).handle(value))
        self.assertEqual("200", DefaultPrecision(5).handle(value))
        self.assertEqual("200", DefaultPrecision(4).handle(value))
        self.assertEqual("200", DefaultPrecision(3).handle(value))
        self.assertEqual("2e+02", DefaultPrecision(2).handle(value))
        self.assertEqual("2e+02", DefaultPrecision(1).handle(value))


class TestFixedPrecision(unittest.TestCase):

    def test_123_456(self):
        value = 123.456
        self.assertEqual("123.456000", FixedPrecision(6).handle(value))
        self.assertEqual("123.45600", FixedPrecision(5).handle(value))
        self.assertEqual("123.4560", FixedPrecision(4).handle(value))
        self.assertEqual("123.456", FixedPrecision(3).handle(value))
        self.assertEqual("123.46", FixedPrecision(2).handle(value))
        self.assertEqual("123.5", FixedPrecision(1).handle(value))
        self.assertEqual("123", FixedPrecision(0).handle(value))

    def test_approximation(self):
        value = 199.999
        self.assertEqual("199.999000", FixedPrecision(6).handle(value))
        self.assertEqual("199.99900", FixedPrecision(5).handle(value))
        self.assertEqual("199.9990", FixedPrecision(4).handle(value))
        self.assertEqual("199.999", FixedPrecision(3).handle(value))
        self.assertEqual("200.00", FixedPrecision(2).handle(value))
        self.assertEqual("200.0", FixedPrecision(1).handle(value))
        self.assertEqual("200", FixedPrecision(0).handle(value))
