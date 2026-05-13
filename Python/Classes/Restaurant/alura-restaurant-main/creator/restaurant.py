from creator.rating import Rating
from menu.menu_item import Menu_item

class Restaurant:
    '''Class Restaurant'''
    r_list = []

    def __init__(self, name, category):
        self._name = name.title()
        self._category = category
        self._active = False
        self._rating = []
        self._menu = []
        Restaurant.r_list.append(self)

    def __str__(self):
        return f'{self.name} | {self.category}'
    
    @classmethod
    def show_all(cls):
        print(f'{'NAME'.ljust(10)} | {'CATEGORY'.ljust(10)} | {'RATING'.ljust(10)} | {'ACTIVE'.ljust(10)}')
        for r in cls.r_list:
            print(f'{r._name.ljust(10)} | {r._category.ljust(10)} | {str(r.avg_rating).ljust(10)} | {r.active.ljust(10)}')

    @property
    def active(self):
        return '☑' if self._active else '☒'
    
    def toggle_active(self):
        self._active = not self._active
        
    def get_rating(self, client, rate):
        rating = Rating(client, rate)
        self._rating.append(rating)

    def get_item(self, item):
        if isinstance(item, Menu_item):
            self._menu.append(item)

    @property
    def avg_rating(self):
        if not self._rating:
            return 'Not rated'
        all_rate = sum(rating._rate for rating in self._rating)
        rate_amm = len(self._rating)
        avg_rate = round(all_rate / rate_amm, 1)

        return avg_rate
    
    @property
    def show_menu(self):
        print(f"> {self._name}'s Menu")
        for i, item in enumerate(self._menu, 1):
            message = f'{i}. | Item: {str(item._name).ljust(10)} | Price: ${str(item._price).ljust(10)}'
            if hasattr(item, 'desc'):
                message += f' | Desc: {item.desc}'
            else:
                message += f' | Size: {item.size}'
            print(message)