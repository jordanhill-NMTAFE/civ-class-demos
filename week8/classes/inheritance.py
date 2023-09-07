"""
    This module demonstrates inheritance
    TODO: Can we implement the tail functionality using inheritance to demonstrate the benefits of composition over inheritance AnimalWithTail vs AnimalWithoutTail classes?
"""


from abc import ABC, abstractmethod
from collections import UserString


# Subtyping Inheritence Example
class String(UserString):
    def __new__(cls, string):
        return super().__new__(cls)

    def is_first_letter_vowel(self):
        vowels = "aeiou"
        vowels = vowels + vowels.upper()
        if any((self[0] == letter for letter in vowels)):
            return True
        else:
            return False


class Animal(ABC):
    type = String("Animal")

    def __init__(self, name: str):
        self.name = name

    # def __init_subclass__(self, name):
    #   super().__init__(self, name)

    @abstractmethod
    def greet(self):
        print("...")

    def has_tail(self):
        # pass
        try:
            return self.tail
        except AttributeError:
            return False


class Human(Animal):
    type = String("Human")

    def greet(self):
        print(
            f"Hi, my name is {self.name}, I am a{'n' if self.type.is_first_letter_vowel() else ''} {self.type}"
        )


class Bird(Animal):
    type = String("Bird")
    tail = True

    def has_tail(self):
        return super().has_tail()

    def greet(self):
        print("SQUUUAAARK!", self.name.upper(), "WANTS A CRACKER!")


class Dog(Animal):
    type = String("Dog")
    tail = True
    quadruped = True

    def greet(self):
        print("Woof!")

    def has_tail(self):
        return super().has_tail()


class Cat(Animal):
    def __init__(self, name):
        """
        If we want to use the __init__() hook to change how the subclass will be initialized
        then we need to makesure to explicitly initialise the abstract class as well before
        making our adjustments:
        """
        super().__init__(name)  # initializes base class
        # Make our additions, like so:
        self.type = String("Cat")
        self.tail = True
        self.quadruped = True

    def greet(self):
        print("Meow!")

    def has_tail(self):
        return super().has_tail()


class Aristotle(Human):
    def __init__(self, name="Aristotle"):
        if name != "Aristotle":
            raise NameError("Aristotle class must have the name Aristotle!")
        super().__init__("Aristotle")
        self.occupation = "Philosopher"
        self.gender = "Man"
        self.ethnos = "Greek"
        self.era = "Ancient"

    def greet(self, aquaintance: Human | None = None):
        if not aquaintance is None:
            print("This is my aquaintance,", aquaintance.name)
        else:
            print(
                "Hello, I am",
                self.name + ".",
                "I am a",
                self.type.lower(),
                self.gender.lower() + ",",
                "I am an",
                self.era,
                self.ethnos,
                self.occupation.lower(),
                "and I like to observe the properties of things.",
            )

    @staticmethod
    def enumerate_and(items: list[String] | set[String]):
        result = []
        for (
            index,
            item,
        ) in enumerate(items):
            if index == len(items) - 1:
                result.append(
                    "an " + item
                    if item.is_first_letter_vowel()
                    else "a " + item
                )
            elif index == len(items) - 2 and len(items) >= 3:
                result.append(
                    "an " + item + ", and"
                    if item.is_first_letter_vowel()
                    else "a " + item + ", and"
                )
            elif index == len(items) - 2:
                result.append(
                    "an " + item + " and"
                    if item.is_first_letter_vowel()
                    else "a " + item + " and"
                )
            else:
                result.append(
                    "an " + item + ","
                    if item.is_first_letter_vowel()
                    else "a " + item + ","
                )

        return result

    @staticmethod
    def enumerate_or(items: list[String] | set[String]):
        result = []
        for (
            index,
            item,
        ) in enumerate(items):
            if index == len(items) - 1:
                result.append(
                    "an " + item
                    if item.is_first_letter_vowel()
                    else "a " + item
                )
            else:
                result.append(
                    "an " + item + "or"
                    if item.is_first_letter_vowel()
                    else "a " + item + " or"
                )

        return result

    def philosophize(self, animals):
        print("Take these animals:")
        with_tails: list[String] = []
        without_tails: list[String] = []
        for animal in animals:
            name = animal.name + " the " + animal.type
            print(
                f"{name} has a tail"
                if animal.has_tail()
                else f"{name} has no tail"
            )
            if animal.has_tail():
                with_tails.append(animal.type)
            else:
                without_tails.append(animal.type)

        print(
            "Therefore, we can say that we have examples of",
            *self.enumerate_and(set(with_tails)),
            "all having tails",
            "and none of",
            *self.enumerate_and(set(without_tails)),
            "having one.",
        )
        print(
            "Therefore, if an animal has a tail it is probably either",
            *self.enumerate_or(set(with_tails)),
            "and if an animal has no tail it must be",
            *self.enumerate_or(set(without_tails)),
            end="",
        )
        print(".")
