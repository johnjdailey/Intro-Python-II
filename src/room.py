#room.py



# Imports

from item import Item


# Implement a class to hold room information. This should have name and
# description attributes.

class Room:
    def __init__(self, name, description, items=None):
        self.name = name
        self.description = description
        self.n_to = None
        self.s_to = None
        self.e_to = None
        self.w_to = None
        self.items = [] if items is None else items

    def __str__(self):
        return f"Room: {self.name}, Description: {self.description}, Items: {self.items}"

    def add_item(self, item):
        self.items.append(item)

    def remove_item(self, item):
        self.items.remove(item)
