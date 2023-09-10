from itertools import product, chain

combine = lambda A, B: [a+b for a,b in product(A,B)]
boxes   = lambda A, B: [combine(a,b) for a,b in product(A, B)]

units = list(chain(
    [combine('ABCDEFGHI', d) for d in '123456789'],     # columns
    [combine(a, '123456789') for a in 'ABCDEFGHI'],     # rows
    [*boxes(['ABC','DEF','GHI'], ['123','456','789'])]  # boxes
))

# Variation
# units = [
#     *[combine('ABCDEFGHI', d) for d in '123456789'],    # columns
#     *[combine(a, '123456789') for a in 'ABCDEFGHI'],    # rows
#     *boxes(['ABC','DEF','GHI'], ['123','456','789'])    # boxes
# ]

# Get all unique cells seen in any of the units.
squares = sorted(set(chain.from_iterable(units)))
print(squares)
for unit in units:
    print(unit)
