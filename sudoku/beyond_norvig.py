# We take the idea of the cross function one step further.
# cross is an abstraction over the idea of adding all pairs of elements from two iterables.
# combine here is the realization that the same idea is used when created boxes, but using cross instead of addition.
# Hence a new function where we can define how to combine the pairs.

# Fun, but needlessly obtuse.
import operator

def combine(A, B, f=operator.add):
    "Combine of elements in A and elements in B where the function f is called on each pair (a,b)."
    return [f(a,b) for a in A for b in B]

cols     = '123456789'
rows     = 'ABCDEFGHI'
squares  = combine(rows, cols)
unitlist = ([combine(rows, c) for c in cols] +
            [combine(r, cols) for r in rows] +
            [*combine(('ABC','DEF','GHI'),('123','456','789'), combine)])

print(squares)
for unit in unitlist:
    print(unit)
