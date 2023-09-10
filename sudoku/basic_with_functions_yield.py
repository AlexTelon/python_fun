# Variation of basic_with_functions.py but using yield and star unpacking.
# So now we use slightly more of the python functionality. Though these are hardy unique to python.

COLS = '123456789'
ROWS = 'ABCDEFGHI'

def squares():
    for r in ROWS:
        for c in COLS:
            yield r+c

print(list(squares()))

def columns():
    for c in COLS:
        col = []
        for r in ROWS:
            col.append(r+c)
        yield col

def rows():
    for r in ROWS:
        row = []
        for c in COLS:
            row.append(r+c)
        yield row

def boxes():
    for rs in ['ABC','DEF','GHI']:
        for cs in ['123','456','789']:
            box = []
            for r in rs:
                for c in cs:
                    box.append(r+c)
            yield box

unitlist = [*columns(), *rows(), *boxes()]
for unit in unitlist:
    print(unit)