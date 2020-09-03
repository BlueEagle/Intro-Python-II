# Write a class to hold player information, e.g. what room they are in
# currently.
import utils


class Player:
    def __init__(self, name, room, items=[]):
        self.name = name
        self.room = room
        self.items = items

    def take_item(self, item_name):
        item_found = False
        for item in self.room.items:
            if (item.name == item_name):
                self.items.append(item)
                self.room.items.remove(item)
                item.on_take()
                item_found = True
        if (not item_found):
            utils.display_text(
                f"You search the room for {item_name}... ooh! some dust!")

    def drop_item(self, item_name):
        item_found = False
        utils.display_text(f"Before loop: {self.room.items}")
        for item in self.items:
            if(item.name == item_name):
                self.room.items.append(item)
                self.items.remove(item)
                item.on_drop()
                item_found = True
        utils.display_text(f"After loop: {self.room.items}")
        if (not item_found):
            utils.display_text(
                f"You empty your pockets and sift through your backpack... There is no {item_name} to be found!")

    def show_inventory(self):
        utils.clear()
        print("Inventory:\n\n")
        for item in self.items:
            print(f"    {item.name} - {item.description}")
        utils.pause()
