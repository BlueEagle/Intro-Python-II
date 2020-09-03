# Write a class to hold player information, e.g. what room they are in
# currently.
class Player:
    def __init__(self, name, room, items=[]):
        self.name = name
        self.room = room
        self.items = items

    def take_item(self, item_name):
        item_found = False
        for item in self.room.items:
            if (item.name == item_name):
                self.room.items.remove(item_name)
