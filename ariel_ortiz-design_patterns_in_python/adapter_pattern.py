# Adapter Pattern
# Structural Design Pattern

import template_method_pattern
from random import randint
# Example


class GeneratorAdapter:
    # Mimics the same naming and return items that would exist if a user used .readline()
    # on a file.

    # Takes in a generator instead of a file... it works like a file but is not.

    def __init__(self, adaptee):
        self.adaptee = adaptee

    def readline(self):
        try:
            return next(self.adaptee)
        except StopIteration:
            return ""

    def close(self):
        pass


# Example Two

class Duck:
    def quack(self):
        print("Quack")

    def fly(self):
        print("I'm Flying.")


class Turkey:
    def gobble(self):
        print("Gobble, gobble")

    def fly(self):
        print("I'm flying a short distance.")


class TurkeyAdapter:
    def __init__(self, adaptee):
        self.adaptee = adaptee

    def quack(self):
        self.adaptee.gobble()

    def fly(self):
        for i in range(5):
            self.adaptee.fly()


def duck_interaction(duck):
    duck.quack()
    duck.fly()


if __name__ == "__main__":
    duck = Duck()
    turkey = Turkey()
    turkey_adapter = TurkeyAdapter(turkey)

    print("The Turkey Says...")
    turkey.gobble()
    turkey.fly()

    print("\nThe Duck Says...")
    duck_interaction(duck)

    print("\nThe TurkeyAdapter Says...")
    duck_interaction(turkey_adapter)

    # Using the adapter
    g = (randint(1, 100) for i in range(1_000))
    fac = template_method_pattern.FileAverageCalculator(GeneratorAdapter(g))
    print(fac.average())