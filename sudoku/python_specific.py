# The solution similar to basic.py but with the addition of list comprehensions.
# To read and understand this you need to be comfortable with how list comprehensions work in python.
# Also the combining of lists with + is not obvious if you are a non-python programmer,
# and most likely not obvious even if you are/

cols = '123456789'
rows = 'ABCDEFGHI'

squares = [r+c for r in rows for c in cols]
print(squares)

unit_cols   = [[r+c for r in rows] for c in cols]
unit_rows   = [[r+c for c in cols] for r in rows]
unit_boxes  = []
for rs in ('ABC','DEF','GHI'):
    for cs in ('123','456','789'):
        unit_boxes.append([r+c for r in rs for c in cs])

unitlist = unit_cols + unit_rows + unit_boxes

for unit in unitlist:
    print(unit)
