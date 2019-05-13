# Observer Pattern
# Behavioral Design Pattern
# Involves a one to many relationship so that its dependants are notified and updated.

from abc import ABC, abstractmethod


class Observer(ABC):

    @abstractmethod
    def update(self, observables, *args):
        pass


class Observable:

    def __init__(self):
        self.__observers = []

    def add_observer(self, observer):
        self.__observers.append(observer)

    def del_observer(self, observer):
        self.__observers.remove(observer)

    def notify_observers(self, *args):
        for o in self.__observers:
            o.update(self, *args)


class Employee(Observable):

    def __init__(self, name, salary):
        super().__init__()
        self._name = name
        self._salary = salary

    @property
    def name(self):
        return self._name

    @property
    def salary(self):
        return self._salary

    @salary.setter
    def salary(self, new_salary):
        self._salary = new_salary
        self.notify_observers(new_salary)


class Payroll(Observable):
    def update(self, changed_employee, new_salary):
        print(f"Cut a new cheque for {changed_employee.name}."
              f"His/her salary is {new_salary}.")


class Taxman(Observable):
    def update(self, changed_employee, new_salary):
        print(f"Send {changed_employee.name} a new Tax Bill!")


class Twitter(Observable, Observer):
    def __init__(self, name):
        super().__init__()
        self.name = name

    def follow(self, observer):
        print(f"{self.name} is now following {observer.name}")
        observer.add_observer(self)
        return self

    def tweet(self, tweet):
        self.notify_observers(tweet)

    def update(self, tweeter, tweet):
        print(f"{self.name} receives a tweet from {tweeter.name}: {tweet}")

def employee_example():
    e = Employee("Amy Fowler Fawcett", 50_000)
    p = Payroll()
    t = Taxman()

    e.add_observer(p)
    e.add_observer(t)

    print("Update 1")
    e.salary = 60_000
    e.del_observer(t)

    print("\nUpdate 2")
    e.salary = 65_000


def twitter_example():
    a = Twitter("Alice")
    k = Twitter("King")
    q = Twitter("Queen")
    h = Twitter("Mad Hatter")
    c = Twitter("Cheshire Cat")

    a.follow(c).follow(h).follow(q)
    k.follow(q)
    q.follow(q).follow(h)
    h.follow(a).follow(q).follow(c)

    print(f"=== {q.name} tweets === ")
    q.tweet("Off with their heads.")

    print(f"\n=== {a.name} tweets === ")
    a.tweet("What a strange world we live in.")

    print(f"\n=== {k.name} tweets === ")
    k.tweet("Begin at the beginning, and go on till you come to the end; then stop.")

    print(f"\n=== {c.name} tweets === ")
    c.tweet("We're all mad here.")

    print(f"\n=== {h.name} tweets === ")
    h.tweet("Why is a raven like a writing-desk?")


if __name__ == "__main__":
    # employee_example()
    twitter_example()

