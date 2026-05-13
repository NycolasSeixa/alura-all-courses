from menu.menu_item import Menu_item

class Drink(Menu_item):
    def __init__(self, name, price, size):
        super().__init__(name, price)
        self.size = size

    def __str__(self):
        return self._name
    
    def get_discount(self):
        self._price -= self._price * 0.08