import utils


class Item:
    def __init__(self, name, description):
        self.name = name
        self.description = description

    def on_take(self):
        utils.display_text(f"You picked up {self.name}!")

    def on_drop(self):
        utils.display_text(f"You dropped {self.name}!")
