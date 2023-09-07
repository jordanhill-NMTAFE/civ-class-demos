"""
  This is the main file used to interact with the class interfaces and actualy execute the desired functionality
  Examples of an implementation of the classes using inheritance is found in classes.inheritance
  Examples of an implementation of the classes using composition is found in classes.composition
"""
# from classes.inheritance import Aristotle
# from classes.composition import Aristotle

from classes.poetry import Poet


def main():
    characters: dict[str, str] = {
        "Betty": "Bird",
        "Casey": "Cat",
        "Derrick": "Dog",
        "Harold": "Human",
        "Aristotle": "Aristotle",
    }

    character_interfaces = Poet("inheritance").make(characters)

    for animal in character_interfaces.values():
        animal.greet()

    aristotle = character_interfaces["Aristotle"]

    aristotle.philosophize(character_interfaces.values())


if __name__ == "__main__":
    main()
