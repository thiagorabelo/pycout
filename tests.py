import unittest

from io import StringIO

from ostream import OStream, endl, ends
from ostream.precisions import Scientific, Fixed
from iomanip import setprecision, setfill, setw


class TestOStream(unittest.TestCase):

    def setUp(self):
        self.output_stream = StringIO()
        self.cout = OStream(output_stream=self.output_stream)

    def tearDown(self):
        self.cout = None
        self.output_stream.close()

    def _get_stream_value(self):
        return self.output_stream.getvalue()

    def test_basic(self):
        # pylint: disable=pointless-statement,expression-not-assigned
        self.cout << "Olá mundo" << " " << "cruel!" << endl << ends

        self.assertEqual("Olá mundo cruel!\n\0", self._get_stream_value())

    def _test_numbers(self):
        # pylint: disable=pointless-statement,expression-not-assigned
        self.cout << 10 << "," << 2.0/5.0 << endl
        self.assertEqual("10,0.4\n", self._get_stream_value())

    def test_setprecicion(self):
        # pylint: disable=pointless-statement,expression-not-assigned
        self.cout << setprecision(3) << 2.0/3.0
        self.assertEqual("0.67", self._get_stream_value())

    def test_set_fill_width(self):
        # pylint: disable=pointless-statement,expression-not-assigned
        self.cout << "ABCD" << "\n" \
                  << setfill("-") << setw(4) \
                  << "EF" << "\n" \
                  << "IJKL" << "\n" \
                  << setfill("-") << setw(4) \
                  << "MNOPQRS\n" \
                  << setfill("-") << setw(4) \
                  << "TU\nVWXYZ"

        string = "ABCD\n" \
                 "--EF\n" \
                 "IJKL\n" \
                 "MNOPQRS\n" \
                 "TU\nVWXYZ"

        self.assertEqual(string, self._get_stream_value())


class TestScentificPrecision(unittest.TestCase):

    def test_123_456(self):
        value = 123.456
        self.assertEqual("123.456", Scientific(6).handle(value))
        self.assertEqual("123.46", Scientific(5).handle(value))
        self.assertEqual("123.5", Scientific(4).handle(value))
        self.assertEqual("123", Scientific(3).handle(value))
        self.assertEqual("1.2e+02", Scientific(2).handle(value))
        self.assertEqual("1e+02", Scientific(1).handle(value))

    def test_approximation(self):
        value = 199.999
        self.assertEqual("199.999", Scientific(6).handle(value))
        self.assertEqual("200", Scientific(5).handle(value))
        self.assertEqual("200", Scientific(4).handle(value))
        self.assertEqual("200", Scientific(3).handle(value))
        self.assertEqual("2e+02", Scientific(2).handle(value))
        self.assertEqual("2e+02", Scientific(1).handle(value))


class TestFixedPrecision(unittest.TestCase):

    def test_123_456(self):
        value = 123.456
        self.assertEqual("123.456000", Fixed(6).handle(value))
        self.assertEqual("123.45600", Fixed(5).handle(value))
        self.assertEqual("123.4560", Fixed(4).handle(value))
        self.assertEqual("123.456", Fixed(3).handle(value))
        self.assertEqual("123.46", Fixed(2).handle(value))
        self.assertEqual("123.5", Fixed(1).handle(value))
        self.assertEqual("123", Fixed(0).handle(value))

    def test_approximation(self):
        value = 199.999
        self.assertEqual("199.999000", Fixed(6).handle(value))
        self.assertEqual("199.99900", Fixed(5).handle(value))
        self.assertEqual("199.9990", Fixed(4).handle(value))
        self.assertEqual("199.999", Fixed(3).handle(value))
        self.assertEqual("200.00", Fixed(2).handle(value))
        self.assertEqual("200.0", Fixed(1).handle(value))
        self.assertEqual("200", Fixed(0).handle(value))


if __name__ == '__main__':
    unittest.main()

#     cout = OStream()  # pylint: disable=invalid-name
#
#     # pylint: disable=pointless-statement, expression-not-assigned
#     cout << "Olá mundo" \
#          << " cruel! " \
#          << 100.123 \
#          << setprecision(2) << "\n" \
#          << "depois do precision\n" \
#          << 100.1234 \
#          << " depois do número" \
#          << endl \
#          << "Hello World\n" \
#          << setfill('*') \
#          << setw(5) \
#          << "a\nb" \
#          << endl
