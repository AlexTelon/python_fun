# Goal here was to create something that anyone with a programming background can read and understand.
# Knowledge of python not required.

cols = '123456789'
rows = 'ABCDEFGHI'

squares = []
for r in rows:
    for c in cols:
        squares.append(r+c)
print(squares)

unitlist = []
# Columns.
for c in cols:
    col = []
    for r in rows:
        col.append(r+c)
    unitlist.append(col)

# Rows.
for r in rows:
    row = []
    for c in cols:
        row.append(r+c)
    unitlist.append(row)

# Boxes.
for rs in ['ABC','DEF','GHI']:
    for cs in ['123','456','789']:
        box = []
        for r in rs:
            for c in cs:
                box.append(r+c)
        unitlist.append(box)

for unit in unitlist:
    print(unit)