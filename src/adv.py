from room import Room
from player import Player
from item import Item
import os
import utils

# Declare all the rooms

room = {
    'outside':  Room("Outside Cave Entrance",
                     "North of you, the cave mount beckons", [Item('teapot', 'I\'m a little teapot!')]),

    'foyer':    Room("Foyer", """Dim light filters in from the south. Dusty
passages run north and east."""),

    'overlook': Room("Grand Overlook", """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm."""),

    'narrow':   Room("Narrow Passage", """The narrow passage bends here from west
to north. The smell of gold permeates the air."""),

    'treasure': Room("Treasure Chamber", """You've found the long-lost treasure
chamber! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south."""),
}


# Link rooms together

room['outside'].n_to = room['foyer']
room['foyer'].s_to = room['outside']
room['foyer'].n_to = room['overlook']
room['foyer'].e_to = room['narrow']
room['overlook'].s_to = room['foyer']
room['narrow'].w_to = room['foyer']
room['narrow'].n_to = room['treasure']
room['treasure'].s_to = room['narrow']


# Additional Features
clear, existence_error, pause, display_text = utils.clear, utils.existence_error, utils.pause, utils.display_text


# TODO: add functionality for combine_additional_args


def combine_additional_args(arg_list, starting_arg):
    return arg_list

#
# Main
#
# Make a new player object that is currently in the 'outside' room.


player = Player('John Doe', room['outside'])

# Write a loop that:
#
# * Prints the current room name
# * Prints the current description (the textwrap module might be useful here).
# * Waits for user input and decides what to do.
#
# If the user enters a cardinal direction, attempt to move to the room there.
# Print an error message if the movement isn't allowed.
#
# If the user enters "q", quit the game.

running = True
while (running):
    clear()
    print(f"Location: {player.room.name}")
    print(player.room.description+"\n")
    if(len(player.room.items) > 0):
        print("Items found in this room!")
        player.room.print_items()
    select = str(
        input('\nYour move buddy!\nMOVE(n,s,w,e) QUIT(q) INVENTORY(i): '))
    select = select.split(" ")
    if (len(select) == 1):
        select = select[0]

    if (isinstance(select, str)):
        if (select == 'q'):  # QUIT
            utils.clear()
            running = False
        if (select == 'n'):  # NORTH
            try:
                player.room = player.room.n_to
            except:
                display_text(existence_error('North'))
        if (select == 's'):  # SOUTH
            try:
                player.room = player.room.s_to
            except:
                display_text(existence_error('South'))
        if (select == 'w'):  # WEST
            try:
                player.room = player.room.w_to
            except:
                display_text(existence_error('West'))
        if (select == 'e'):  # EAST
            try:
                player.room = player.room.e_to
            except:
                display_text(existence_error('East'))
        if (select == 'i' or select == 'inventory'):
            player.show_inventory()
    else:
        if(select[0] == 'get'):
            select = combine_additional_args(select, 1)
            player.take_item(select[1])
        if(select[0] == 'drop'):
            select = combine_additional_args(select, 1)
            player.drop_item(select[1])
