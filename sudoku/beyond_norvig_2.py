# Here are some more variations where we define various functions/abstractions.
import operator
from itertools import product

# Alternative 1.
combine = lambda A, B: [operator.add(a,b) for a,b in product(A,B)]
boxes   = lambda A, B: [combine(a,b) for a,b in product(A, B)]

# Alternative 2.
# apply   = lambda A, B, f: [f(a,b) for a,b in product(A,B)]
# combine = lambda A, B: apply(A, B, operator.add)
# boxes   = lambda A, B: apply(A, B, combine)

# Alternative 3.
# from functools import partial
# apply   = lambda A, B, f: [f(a,b) for a,b in product(A,B)]
# combine = partial(apply, f=operator.add)
# boxes   = partial(apply, f=combine)

cols = '123456789'
rows = 'ABCDEFGHI'

squares = combine(rows, cols)
unitlist = ([combine(rows, c) for c in cols] +
            [combine(r, cols) for r in rows] +
            [*boxes(('ABC','DEF','GHI'),('123','456','789'))])

print(squares)
for unit in unitlist:
    print(unit)
