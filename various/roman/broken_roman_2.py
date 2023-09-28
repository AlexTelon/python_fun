from itertools import pairwise

n = int(input())

value_to_roman = {
    1000: 'M',
    # 900: 'CM',
    500: 'D',
    # 400: 'CD',
    100: 'C',
    # 90: 'XC',
    50: 'L',
    # 40: 'XL',
    10: 'X',
    # 9: 'IX',
    5: 'V',
    # 4: 'IV',
    1: 'I',
}

res = ''
while n:
    for value, roman in value_to_roman.items():
        if value <= n:
            res += roman
            n -= value
            break
# print('original', res)

# replace 4 instances of a char (say IIII) with one instance of it and then one of the next higher one.
for a, b in pairwise(reversed(value_to_roman.values())):
    res = res.replace(a*4, a+b)

# bah we still get some bad stuff...

# # 9 -> VIIII -> VIV -> IV
# for a, b in pairwise(reversed(value_to_roman.values())):
#     res = res.replace(b+a+b, a+b)

print(res)