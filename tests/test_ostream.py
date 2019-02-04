import unittest

from io import StringIO

from ostream import OStream, endl, ends
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

    def test_numbers(self):
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

    def test_complex_stream(self):
        # pylint: disable=pointless-statement,expression-not-assigned
        self.cout << "Olá mundo" \
                  << " cruel! " \
                  << 100.123 \
                  << setprecision(2) << "\n" \
                  << "depois do precision\n" \
                  << 100.1234 \
                  << " depois do número" \
                  << endl \
                  << "Hello World\n" \
                  << setfill('*') \
                  << setw(5) \
                  << "a\nb" \
                  << endl

        string = "Olá mundo cruel! 100.123\n" \
                 "depois do precision\n" \
                 "1e+02" \
                 " depois do número\n" \
                 "Hello World\n" \
                 "**a\n" \
                 "b\n"

        self.assertEqual(string, self._get_stream_value())
