from creator.restaurant import Restaurant

from menu.drink import Drink
from menu.plate import Plate

plaza = Restaurant('Plaza', 'Pizza')

coke = Drink('Coke', 5.0, '250ml')
coke.get_discount()

xburguer = Plate('X-burguer', 2.0, 'Bread and Hamburguer')
xburguer.get_discount()

plaza.get_item(coke)
plaza.get_item(xburguer)

def main():
    plaza.show_menu     

if __name__ == '__main__':
    main()

