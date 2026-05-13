from menu.menu_item import Menu_item

class Plate(Menu_item):
    def __init__(self, name, price, desc):
        super().__init__(name, price)
        self.desc = desc

    def __str__(self):
        return self._name

    def get_discount(self):
        self._price -= self._price * 0.05