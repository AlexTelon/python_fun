# hard but simple.
# Hard because it teaches you about a cross-product. 
# The first time you see it you will say "hold up, whats this?"
# But once you understand it the rest of the code is simple.



# https://norvig.com/sudoku.html
def cross(A, B):
    "Cross product of elements in A and elements in B."
    return [a+b for a in A for b in B]

digits   = '123456789'
rows     = 'ABCDEFGHI'
cols     = digits
squares  = cross(rows, cols)
unitlist = ([cross(rows, c) for c in cols] +
            [cross(r, cols) for r in rows] +
            [cross(rs, cs) for rs in ('ABC','DEF','GHI') for cs in ('123','456','789')])

print(squares)
for unit in unitlist:
    print(unit)