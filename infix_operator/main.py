from functools import partial

class Infix():
    def __init__(self, func):
        self.func = func

    # Define left and right or.
    #one allows:
    # 5 | thing
    # the other:
    # thing | 5
    # together:
    # 5 |thing| 5

    # ror has precedence. So it will run first.
    # The same is possible with other operators like *.
    # See other alternatives here: https://docs.python.org/3/reference/datamodel.html#emulating-numeric-types
    # Since the different operators have different precedence it might be good to play around with that
    # See https://docs.python.org/3/reference/expressions.html#operator-precedence

    def __or__(self, other):
        return self.func(other)

    def __ror__(self, other):
        return Infix(partial(self.func, other))

    def __mul__(self, other):
        return self.func(other)

    def __rmul__(self, other):
        return Infix(partial(self.func, other))

    # Allows for `@Infix` decoration of functions.
    # Otherwise you would have to manually use something like:
    # def add(x,y):
    #     return x + y
    # addd = Infix(add)
    #
    # Instead of simply
    # @Infix
    # def add(x,y):
    #     return x + y
    #
    def __call__(self, a, b):
        return self.func(a, b)

@Infix
def add(x,y):
    return x + y

print(5 |add| 6)
print(5 *add* 6)