# Template Method
# - behavioral design pattern
# - allows a base structure to exist, but certain components can be changed.
# - This example is based around an 'average calculator'
# - Note the ABC class - anything that uses the @abstractmethod decorator means the
#   derived class will need to implement that function.

from abc import ABC, abstractmethod


class AverageCalculator(ABC):
    def average(self):
        try:
            num_items = 0
            total_sum = 0
            while self.has_next():
                total_sum += self.next_item()
                num_items += 1

            if num_items == 0:
                raise RuntimeError("Can't compute the average of zero items.")
            return total_sum / num_items
        finally:
            self.dispose()

    @abstractmethod
    def has_next(self):
        pass

    @abstractmethod
    def next_item(self):
        pass

    def dispose(self):
        """User inheriting this class is NOT forced to replace it."""
        pass


class FileAverageCalculator(AverageCalculator):
    def __init__(self, file):
        self.file = file
        self.last_line = self.file.readline()

    def has_next(self):
        return self.last_line != ""

    def next_item(self):
        result = float(self.last_line)
        self.last_line = self.file.readline()
        return result

    def displose(self):
        self.file.close()


class MemoryAverageCalculator(AverageCalculator):
    def __init__(self, items):
        self.items = iter(items)
        self.next = next(self.items, None)

    def has_next(self):
        return self.next is not None

    def next_item(self):
        result = float(self.next)
        self.next = next(self.items, None)
        return result


if __name__ == "__main__":
    fac = FileAverageCalculator(open("data.txt"))
    print(fac.average())

    mac = MemoryAverageCalculator([3, 1, 4, 1, 5, 9, 2, 6, 5, 3])
    print(mac.average())  # 3.9
