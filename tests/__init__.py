import unittest

from .test_precision import TestFixedPrecision, TestScentificPrecision
from .test_ostream import TestOStream
from .test_intbase import TestIntHandler


__ALL__ = tuple((
    'TestFixedPrecision TestScentificPrecision '
    'TestOStream '
    'TestIntHandler'
).strip().split())
