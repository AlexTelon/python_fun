n = int(input())

value_to_roman = {
    0: '',
    1: 'I',
    4: 'IV',
    5: 'V',
    9: 'IX',
    10: 'X',
    40: 'XL',
    50: 'L',
    90: 'XC',
    100: 'C',
    400: 'CD',
    500: 'D',
    900: 'CM',
    1000: 'M',
}
values = list(value_to_roman.keys())
while value := values.pop():
    x, n = divmod(n, value)
    print(end=value_to_roman[value] * x)