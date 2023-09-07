from abc import ABC, abstractmethod

class Tail:
    type = "Tail"

    def exists(self):
        return True

    def twirl(self):
        print("*Swiiiish Swooosh*")


class Animal(ABC):
    type = "Animal"

    def __init__(self, name):
        self.name = name

    @abstractmethod
    def greet(self):
        pass

    def confirm_existance(self, thing):
        try:
            return thing.exists()
        except (AttributeError, NameError):
            return False

    def has_tail(self):
        try:
            return self.tail.exists()
        except (AttributeError, NameError):
            return False


class Human(Animal):
    type = "Human"

    def greet(self):
        print("Hi my name is", self.name, "I am a", self.type)

class Cat(Animal):
    type = "Cat"
    def __init__(self, name):
        super().__init__(name)
        self.tail = Tail()
    def greet(self):
        print("Meow")

bob = Human("Bob")
bob.greet()

tom = Cat("Tom")

tom.greet()

if tom.has_tail():
    print("Tom has a tail")
else:
    print("Tom has no tail")

if bob.has_tail():
    print("Bob has a tail")
else:
    print("Bob has no tail")

if tom.has_tail():
    tom.tail.twirl()

