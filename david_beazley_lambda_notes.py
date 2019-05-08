# NO IFs, NO numbers, Only functions
# - can we create something with the narrow set of rules?


# Can we create switch functions?
def LEFT(a):
    def f(b):
        return a

    return f


def RIGHT(a):
    def f(b):
        return b

    return f


# BOOL
def TRUE(x):
    return lambda y: x


def FALSE(x):
    return lambda y: y


def NOT(x):
    return x(FALSE)(TRUE)


def AND(x):
    """
    print(6 and 3)
    >>> 3
    print(0 and 3)
    >>> 0
    """
    return lambda y: x(y)(x)


def OR(x):
    return lambda y: x(x)(y)


# Lets represent numbers!


# - how do young kids learn about numbers? Finger counting? Visualization? Score marks?
# - Example using something referred to as The ChurchNumerals:
ONE = lambda f: lambda x: f(x)
TWO = lambda f: lambda x: f(f(x))
THREE = lambda f: lambda x: f(f(f(x)))
FOUR = lambda f: lambda x: f(f(f(f(x))))

# define ZERO
# - There is an API -- strict rules -- you take an f and take an x -- if those aren't there then its a zero
ZERO = lambda f: lambda x: x

# Challenge: Implement successor
# SUCC(TWO) --> THREE
SUCC = lambda n: lambda f: lambda x: f(n(f)(x))

# Challenge #2: Implement Add, Multiply
ADD = lambda x: lambda y: y(SUCC)(x)
MUL = lambda x: lambda y: lambda f: y(x(f))

# DIGRESSION

data = {"a": {"b": {"c": 42}}}


def getc(d):
    return d["a"]["b"]["c"]


print("#1 getc():", getc(data))
# print(getc({}))  # <-- this will fail with a KeyError


def getc(d):
    # This one is defensive...
    d = d.get("a")
    if d is not None:
        d = d.get("b")
    if d is not None:
        d = d.get("c")
    return d


print("#2 getc():", getc(data))
print("#2 getc() - Expecting None: ", getc({}))  # No longer produced a KeyError


def perhaps(d, func):
    if d is not None:
        return func(d)
    else:
        return None


perhaps(data, lambda d: d.get("a"))

result = perhaps(
    perhaps(perhaps(data, lambda d: d.get("a")), lambda d: d.get("b")),
    lambda d: d.get("c"),
)
print("#3 perhaps: ", result)


class Perhaps:
    # 'Perhaps' this is an example of a monad
    def __init__(self, value):
        self.value = value

    def __rshift__(self, other):
        if self.value is not None:
            return Perhaps(other(self.value))
        else:
            return self


result = (
    Perhaps(data)
    >> (lambda d: d.get("a"))
    >> (lambda d: d.get("b"))
    >> (lambda d: d.get("c"))
)
print("#4 Perhaps: ", result.value)

# The CONVERSIONS
# - RULE #1: You can rename an argument
#            Caveat: You cannot introduce a name clash
#            Known as: "Alpha Conversion"
# - Rule #2: You can substitute arguments
#            Caveat: You cannot introduce a name clash
#            Python example:
#               x = 3
#               y = 4
#               def f(x, y): return 2*x + y  # does outer x, y effect function scope? No.
# - Rule #3: You can make a function
#            Python example:
#               x = 3
#               x = (lambda a: a)(3)
#               >>> 3

# The Reverse
# Can you subtract?
# Use pairs?
# (0, 0)
# (1, 0)
# (2, 1)
# (3, 2)


CONS = lambda a: lambda b: (lambda s: s(a)(b))
p = CONS(2)(3)
CAR = lambda p: p(TRUE)
CDR = lambda p: p(FALSE)

if __name__ == "__main__":

    # Examples of currying
    print(f"{LEFT('5v')('ground')}")
    print(f"{RIGHT('5v')('ground')}")

    # These are behaviors rather than data structure
    print(f"{TRUE('T')('F')}")
    print(f"{FALSE('T')('F')}")

    #
    assert NOT(TRUE) is FALSE
    assert NOT(FALSE) is TRUE

    assert AND(TRUE)(TRUE) is TRUE
    assert AND(TRUE)(FALSE) is FALSE
    assert AND(FALSE)(FALSE) is FALSE
    assert AND(FALSE)(TRUE) is FALSE

    assert OR(TRUE)(TRUE) is TRUE
    assert OR(TRUE)(FALSE) is TRUE
    assert OR(FALSE)(TRUE) is TRUE
    assert OR(FALSE)(FALSE) is FALSE

    # Func to help demonstrate what is going on with counting -- but is only for illustration purposes
    # - it breaks the rules of only functions and single arguments and no numbers, etc.
    def incr(x):
        return x + 1

    result = ADD(FOUR)(THREE)
    print(result(incr)(0))

    result = MUL(FOUR)(THREE)
    print(result(incr)(0))

    p = CONS(2)(3)
    assert p(TRUE) == 2
    assert p(FALSE) == 3
