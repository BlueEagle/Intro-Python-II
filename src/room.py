# Implement a class to hold room information. This should have name and
# description attributes.
class Room:
    def __init__(self, name, description, items=[]):
        self.name = name
        self.description = description
        self.items = items

    def print_items(self):
        for item in self.items:
            print(f"    {item.name} - {item.description}")
