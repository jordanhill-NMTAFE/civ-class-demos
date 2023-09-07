"""
You don't need to understand how this code works
"""
# These modules are called dynamically using eval() by the make() function
from classes import inheritance, composition

from decimal import Decimal

Decimal()


class Poet:
    """Construct a new Poet object takes a module name and then uses that module to make objects either using composition or inheritance using Poet.make()"""

    def __init__(self, module: str):
        """
        Parameters
        ----------
        module: str

        Returns
        -------
        Poet"""
        if not module == "inheritance" or module == "composition":
            raise ModuleNotFoundError("The requested module does not exist")
        self.module = module

    def make(self, materials: dict[str, str]):
        objects = {}
        for name, form in materials.items():
            try:
                objects[name] = eval(self.module + "." + form + f'("{name}")')
            except Exception as e:
                print(e)
        return objects
