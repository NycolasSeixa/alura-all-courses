from abc import ABC, abstractmethod

class Menu_item(ABC):
    def __init__(self, name, price):
        self._name = name
        self._price = price

    @abstractmethod
    def get_discount(self):
        pass