#player.py



# Imports

from item import Item


# Write a class to hold player information, e.g. what room they are in
# currently.

class Player():
    def __init__(self, name, current_room, inventory=None):
        self.name = name
        self.current_room = current_room
        self.inventory = [] if inventory is None else inventory

    def __str__(self):
        return f"Name: {self.name}, Current Location: {self.current_room}, Inventory: {self.inventory}"

    def add_item(self, item):
        self.inventory.append(item)

    def remove_item(self, item):
        self.inventory.remove(item)
