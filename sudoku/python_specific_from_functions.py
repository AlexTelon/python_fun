# Variation of basic_with_functions_yield_comprehensions.py
# I now add another layer of list comprehensions. In general Im vary if nested loops in comprehensions.
# But the short functions and their names make the code quite understandable imo.
# However I might be biased now since I know the problem well as I have written many many solutions now.

COLS = '123456789'
ROWS = 'ABCDEFGHI'

def squares():
    return [r+c for r in ROWS for c in COLS]

print(squares())

def columns():
    return [[r+c for r in ROWS] for c in COLS]

def rows():
    return [[r+c for c in COLS] for r in ROWS]

def boxes():
    # Nope, not going to use a list comprehension here.
    result = []
    for rs in ['ABC','DEF','GHI']:
        for cs in ['123','456','789']:
            result.append([r+c for r in rs for c in cs])
    return result

unitlist = columns() + rows() + boxes()
for unit in unitlist:
    print(unit)
