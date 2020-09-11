#adv.py



#Imports

from room import Room
from player import Player
from item import Item


# Declare all the items

items = {
    "Lambda Labs Tensorbook": Item("Lambda Labs Tensorbook",
                                   "GPU laptop built for deep learning. Powered by the NVIDIA RTX 2080 Super Max-Q GPU. Pre-installed with TensorFlow, PyTorch, Keras, CUDA, and cuDNN"),

    "Solar Panels":           Item("Solar Panels",
                                   "This 2000 Watt portable solar array could be useful for your Tensorbook, or whatever you want"),

    "Jet Pack":               Item("Jet Pack",
                                   "USAF jetpack, full of fuel"),

    "Laser Pickaxe":          Item("Laser Pickaxe",
                                   "A laser pickaxe designed for mining gold"),

    "Tesla Cyber Truck":      Item("Tesla Cybertruck",
                                   "Fully loaded Cybertruck, great for finding treasure!")
}


# Declare all the rooms

room = {
    'outside':  Room("Outside Cave Entrance",
                     "North of you, the cave mount beckons",
                     "Lambda Labs Tensorbook"), #[tensorbook]

    'foyer':    Room("Foyer", 
                     """Dim light filters in from the south. Dusty passages run north and east.""",
                     "Solar Panels"),

    'overlook': Room("Grand Overlook", 
                     """A steep cliff appears before you, falling into the darkness. Ahead to the north, a light flickers in
                     the distance, but there is no way across the chasm.""",
                     "Jet Pack"),

    'narrow':   Room("Narrow Passage", 
                     """The narrow passage bends here from west to north. The smell of gold permeates the air.""",
                     "Laser Pickaxe"),

    'treasure': Room("Treasure Chamber", 
                     """You've found the long-lost treasure chamber! Sadly, it has already been completely emptied by
                     earlier adventurers. The only exit is to the south.""",
                     "Tesla Cyber Truck"),
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

player_1 = Player("Data Scientist", room[("outside")])


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

    print("\nItems in this location:\n", player_1.current_room.items)

    #available_items = []
    #for item in player_1.current_room.items:
    #    available_items.append(item.name)
    #if len(available_items)==0:
    #    print("\nItems in this location: None")
    #else:
    #    print("\nItems in this location:")
    #    for item in available_items:
    #        print(item)

    # * Waits for user input and decides what to do.

    cmd = input("\nPress 'N', 'S', 'E', 'W' to move to a different room, 'I' to access your inventory, or 'Q' will quit the game\n")

    # If the user enters a cardinal direction, attempt to move to the room there.
    # Print an error message if the movement isn't allowed.

    if len(cmd.split())==1:
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
    
        # If the user enters "q", quit the game.
    
        elif cmd == 'q':
            print("Quitter's never win!")
            break
    
    
        # Open the player inventory
    
        if (cmd == 'i') | (cmd == "inventory"):
            print("Your inventory:")
            for item in player_1.inventory:
                print(item.name)


        # Print an error message if the movement isn't allowed.

        else:
            print("That movement is not allowed. Try another move")


    # Commands and logic for items

    elif len(cmd.split())==2:
        verb= cmd.split()[0]
        selected_item = cmd.split()[1]
        actions = ["take", "drop"]
        if verb in actions:
            if verb == "take":
                if selected_item in player_1.current_room.items: #available_items:
                    player_1.add_item(room.items[selected_item])
                    room.items[selected_item].on_take()
                    available_items = player_1.current_room.remove_item(room.items[selected_item])
                else:
                    print("The item you selected is not in this room")
            elif verb == "drop":
                inventory_items = []
                for item in player_1.inventory:
                    inventory_items.append(item.name)
                if selected_item in inventory_items:
                    player_1.current_room.add_item(room.items[selected_item])
                    player_1.remove_item(room.items[selected_item])
                    room.items[selected_item].on_drop()
                else:
                    print("That item is not in your inventory")
