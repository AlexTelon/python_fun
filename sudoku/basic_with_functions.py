# A variation of basic.py with functions for naming the various parts.
# Still no special python stuff. (beyond .extend for lists)

COLS = '123456789'
ROWS = 'ABCDEFGHI'

def squares():
    result = []
    for r in ROWS:
        for c in COLS:
            result.append(r+c)
    return result

print(squares())


def columns():
    result = []
    for c in COLS:
        col = []
        for r in ROWS:
            col.append(r+c)
        result.append(col)
    return result

def rows():
    result = []
    for r in ROWS:
        row = []
        for c in COLS:
            row.append(r+c)
        result.append(row)
    return result

def boxes():
    result = []
    for rs in ['ABC','DEF','GHI']:
        for cs in ['123','456','789']:
            box = []
            for r in rs:
                for c in cs:
                    box.append(r+c)
            result.append(box)
    return result

unitlist = []
unitlist.extend(columns())
unitlist.extend(rows())
unitlist.extend(boxes())
for unit in unitlist:
    print(unit)