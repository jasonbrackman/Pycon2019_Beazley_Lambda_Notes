# Singleton Example
# - using lazy initialization - if its never needed its never instantiated.
# - Note that this is not thread safe


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


class Singleton:
    _instance = None

    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = object.__new__(cls, *args, **kwargs)
        return cls._instance

class TiggerNew(Singleton):
    pass



if __name__ == "__main__":
    # hacky setup
    a = Tigger()
    b = Tigger()

    print(f"ID(a) == {id(a)}")
    print(f"ID(b) == {id(b)}")
    print(f"Are they the same object? {a is b}")

    # metaclasses
    a = TiggerNew()
    b = TiggerNew()

    print(f"ID(a) == {id(a)}")
    print(f"ID(b) == {id(b)}")
    print(f"Are they the same object? {a is b}")