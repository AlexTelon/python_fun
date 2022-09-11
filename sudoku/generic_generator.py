from itertools import product, zip_longest
import re

cols = '123456789'
rows = 'ABCDEFGHI'

combine = lambda A, B: [a+b for a,b in product(A,B)]
boxes   = lambda A, B: [combine(a,b) for a,b in product(A, B)]
is_window = lambda x: re.match(r':\d+', x)

def grouper(iterable, n, *, incomplete='ignore', fillvalue=''):
    # From https://docs.python.org/3/library/itertools.html#itertools-recipes
    args = [iter(iterable)] * n
    if incomplete == 'fill':
        return map(''.join, zip_longest(*args, fillvalue=fillvalue))
    if incomplete == 'strict':
        return map(''.join, zip(*args, strict=True))
    if incomplete == 'ignore':
        return map(''.join, zip(*args))
    else:
        raise ValueError('Expected fill, strict, or ignore')

def thing(op):
    """A thing that converts expressions like :3:3 or A: or :1 to set of groups from the rows+columns."""
    # Not saying this is great, but it was fun.
    # I should seperate the betweeh :3:3 and :3 etc. 3 here is select 3 at a time or the row 3 depending on context.
    match [*op]:
        case ':', a, ':', b:
            return [combine(r, c) for r in grouper(rows, int(a)) for c in grouper(cols, int(b))]
        case a, ':', b:
            return [combine(rows, c) for c in grouper(cols, int(b))]
        case ':', a, b:
            return [combine(r, cols) for r in grouper(rows, int(a))]
        case ':', ':':
            return combine(rows, cols)
        case ':', c:
            return combine(rows, c)
        case r, ':':
            return combine(r, cols)
        case _:
            raise NotImplementedError(f"{op} not allowed!")


assert thing('::3') == thing(':9:3')
assert list(grouper('AB', 3)) == []
assert list(grouper('ABC', 3)) == ['ABC']
assert list(grouper('ABCDE', 3)) == ['ABC']
assert list(grouper(rows, 3)) == ['ABC', 'DEF', 'GHI']

squares = thing('::')
unitlist = ([thing(':'+c) for c in cols] +
            [thing(r+':') for r in rows] +
            [*thing(':3:3')])

print(squares)
for unit in unitlist:
    print(unit)
