n = int(input())
# value_to_roman = {
#     1000: 'M',
#     900: 'CM',
#     500: 'D',
#     400: 'CD',
#     100: 'C',
#     90: 'XC',
#     50: 'L',
#     40: 'XL',
#     10: 'X',
#     9: 'IX',
#     5: 'V',
#     4: 'IV',
#     1: 'I',
# }
value_to_roman = [(0, ''), (1, 'I'), (4, 'IV'), (5, 'V'), (9, 'IX'), (10, 'X'), (40, 'XL'), (50, 'L'), (90, 'XC'), (100, 'C'), (400, 'CD'), (500, 'D'), (900, 'CM'), (1000, 'M')]
# values = [v for v,_ in value_to_roman]
# romans = [r for _,r in value_to_roman]
# values = [0, 1, 4, 5, 9, 10, 40, 50, 90, 100, 400, 500, 900, 1000]
# romans = ['', 'I', 'IV', 'V', 'IX', 'X', 'XL', 'L', 'XC', 'C', 'CD', 'D', 'CM', 'M']

try:
    while pair := value_to_roman.pop():
        value, roman = pair
        if value <= n:
            print(end=roman)
            n -= value
except IndexError:
    ...