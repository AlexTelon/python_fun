from glob import glob

import pytest
from io import StringIO
import sys

IGNORE_PREFIXES = ['test_', 'broken_']

@pytest.mark.parametrize("n,expected", [
    (1, 'I'),
    (4, 'IV'),
    (9, 'IX'),
    (42, 'XLII'),
    (99, 'XCIX'),
    (500, 'D'),
    (900, 'CM'),
    (1000, 'M'),
    (1987, 'MCMLXXXVII')
])
def test_int_to_roman(n, expected):
    for fname in glob('*.py'):
        if any(map(fname.startswith, IGNORE_PREFIXES)): continue
        sys.stdin = StringIO(str(n))
        sys.stdout = StringIO()
        exec(open(fname).read())
        assert sys.stdout.getvalue() == expected + '\n'
