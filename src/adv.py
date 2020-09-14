#adv.py



#Imports

from room import Room
from player import Player
from item import Item


# Declare all the items

items = {
    "Applesauce":            Item("Applesauce",
                                   "So sweet and so good!"),

    "LambdaLabsTensorbook":  Item("Lambda Labs Tensorbook",
                                   "GPU laptop built for deep learning. Powered by the NVIDIA RTX 2080 Super Max-Q GPU. Pre-installed with TensorFlow, PyTorch, Keras, CUDA, and cuDNN"),

    "SolarPanels":           Item("Solar Panels",
                                   "This 2000 Watt portable solar array could be useful for your Tensorbook, or whatever you want to power"),

    "JetPack":               Item("Jet Pack",
                                   "USAF jetpack, full of fuel and ready to fly"),

    "LaserPickaxe":          Item("Laser Pickaxe",
                                   "A laser pickaxe designed for mining gold"),

    "TeslaCybertruck":       Item("Tesla Cybertruck",
                                   "Fully loaded Cybertruck, great for finding treasure!")
}


# Declare all the rooms

room = {
    'outside':  Room("Outside Cave Entrance",
                     "North of you, the cave mount beckons",
                     [items["LambdaLabsTensorbook"]]),

    'foyer':    Room("Foyer", 
                     """Dim light filters in from the south. Dusty passages run north and east.""",
                     [items["SolarPanels"]]),

    'overlook': Room("Grand Overlook", 
                     """A steep cliff appears before you, falling into the darkness. Ahead to the north, a light flickers in
                     the distance, but there is no way across the chasm.""",
                     [items["JetPack"]]),

    'narrow':   Room("Narrow Passage", 
                     """The narrow passage bends here from west to north. The smell of gold permeates the air.""",
                     [items["LaserPickaxe"]]),

    'treasure': Room("Treasure Chamber", 
                     """You've found the long-lost treasure chamber! Sadly, it has already been completely emptied by
                     earlier adventurers. The only exit is to the south.""",
                     [items["TeslaCybertruck"]]),
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


#
# Main
#


# Make a new player object that is currently in the 'outside' room.

player_1 = Player("Data Scientist", room[("outside")], ["Applesauce"])


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


# Write a loop that:

while True:
    player_1.current_room


    # * Prints the current room name

    print("\nYou are currently at location:\n", player_1.current_room.name)
    

    # * Prints the current description (the textwrap module might be useful here).

    print("\nDescription:\n", player_1.current_room.description)


    # * Prints the items in the current room

    #print("\nItems in this location:\n", player_1.current_room.items) # Using below logic to avoid items persisting

    available_items = []
    for item in player_1.current_room.items:
        available_items.append(item.name)
    if len(available_items)==0:
        print("\nItems in this location: None")
    else:
        print("\nItems in this location:")
        for item in available_items:
            print(item)


    # * Waits for user input and decides what to do.

    cmd = input("\nPress 'N', 'S', 'E', 'W' to move to a different room, 'I' to access your inventory, 'take [item]' to pick up an item, 'drop [item]' to drop an item, or 'Q' to quit the game\n")


    # If the user enters a cardinal direction, attempt to move to the room there.
    # Print an error message if the movement isn't allowed.

    if cmd == "n":
        print("\nGoing north...\n")
        if player_1.current_room.n_to is None:
            print("### There is no room north of you, select a different direction. ###")
        else:
            player_1.current_room = player_1.current_room.n_to

    elif cmd == "s":
        print("\Going south...\n")
        if player_1.current_room.s_to is None:
            print("### There is no room south of you, select a different direction. ###")
        else:
            player_1.current_room = player_1.current_room.s_to

    elif cmd == "e":
        print("\Going east...\n")
        if player_1.current_room.e_to is None:
            print("### There is no room east of you, select a different direction. ###")
        else:
            player_1.current_room = player_1.current_room.e_to

    elif cmd == "w":
        print("\Going west...\n")
        if player_1.current_room.w_to is None:
            print("### There is no room west of you, select a different direction. ###")
        else:
            player_1.current_room = player_1.current_room.w_to


    # Open the player inventory

    elif (cmd == 'i') | (cmd == "inventory"):
        print("Your Inventory:", player_1.inventory)


    # Take and drop items

    elif cmd == f'take {item}':
        player_1.current_room.remove_item(player_1.current_room.items[0])
        player_1.add_item(item)
        print(f"Added {item} to your inventory.")

    elif cmd == f'drop {item}':
        #player_1.current_room.add_item(player_1.inventory[1])
        player_1.remove_item(item)
        print(f'Dropped {item} from your inventory.')

    
    # If the user enters "q", quit the game.

    elif cmd == 'q':
        print("Quitter's never win!")
        break


    # Print an error message if the movement isn't allowed.

    else:
        print("That movement is not allowed. Try another move")
