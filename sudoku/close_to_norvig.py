# This solution moves closer to norvigs by introducing a function for something often repeated before.
# The fact that this was often repeated is much clearer in the shorter python_specific.py solution that used list comprehensions
# than the basic.py solution I think. This is essentially his solution with trivial changes only.

# Norvig calls it cross product, but I think i really is a its a cartesian product.
# Cartesian is harder to spell however and it both cartesian/cross are nonetheless abuses of the terminology
# since we dont return the pair (a,b) but a+b. I will call it combine here.

# Also while I often dislike nested loops in list comprehensions it feels more ok in cases where the order of the two does not matter.
# So for unit_boxes below it would only affect the order in which the unit boxes are given which might not matter here.
# But it depends on how the code is used. For instance my compare.py would fail this file if we did.

def combine(A, B):
    return [a+b for a in A for b in B]

cols = '123456789'
rows = 'ABCDEFGHI'

squares     = combine(rows, cols)
unit_cols   = [combine(rows, c) for c in cols]
unit_rows   = [combine(r, cols) for r in rows]
unit_boxes  = [combine(rs, cs) for rs in ('ABC','DEF','GHI') for cs in ('123','456','789')]
unitlist = unit_cols + unit_rows + unit_boxes

print(squares)
for unit in unitlist:
    print(unit)
