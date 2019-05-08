# covers:
#   idioms - language specific,
#   architectural patterns - big picture,
#   design patterns - can use across many languages
#


#  IDIOMS
# example:

x = 100
# Instead of this
if 0 < x and x < 10:
    pass

# use a simplified chained expression
if 0 < x < 10:
    pass

# ARCHITECTURAL PATTERNS
# Design Principles:
# 1. Separate out things that change from that which stays the same.
# 2. Program to an interface not an implementation.
# 3. Prefer composition over inheritance.
# 4. Delegation
#
# Anatomy of a Design Pattern
# 1. Intent
# 2. Motivation
# 3. Structure
# 4. Implementation


# SINGLETON
# - easy to understand
# - creational design pattern
# - provide a mechanism to access in a global way
# -

# tigger.py

class _Tigger:
    def __str__(self):
        return "I'm the only one."

    def roar(self):
        return "Grrr!"


_instance = None


def Tigger():
    """Creating the illusion of the class, but its just abstracting the global."""
    global _instance
    if _instance is None:
        _instance = _Tigger()
    return _instance


if __name__ == "__main__":
    a = Tigger()
    b = Tigger()
    
    print(f"ID(a) == {id(a)}")
    print(f"ID(b) == {id(b)}")
    print(f"Are they the same object? {a is b}")