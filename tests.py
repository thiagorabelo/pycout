
from ostream import OStream, endl
from iomanip import setprecision, setfill, setw


if __name__ == '__main__':
    cout = OStream()  # pylint: disable=invalid-name

    # import time

    # pylint: disable=pointless-statement
    # pylint: disable=expression-not-assigned
    cout << "Olá mundo" \
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

    # time.sleep(3)
