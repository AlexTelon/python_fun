# Variation based on basic_with_functions_yield_comprehensions.py

COLS = '123456789'
ROWS = 'ABCDEFGHI'

def squares():
    for r in ROWS:
        for c in COLS:
            yield r+c

print(list(squares()))

def columns():
    for c in COLS:
        yield [r+c for r in ROWS]

def rows():
    for r in ROWS:
        yield [r+c for c in COLS]

def boxes():
    for rs in ['ABC','DEF','GHI']:
        for cs in ['123','456','789']:
            yield [r+c for r in rs for c in cs]

unitlist = [*columns(), *rows(), *boxes()]
for unit in unitlist:
    print(unit)