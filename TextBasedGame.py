# Nik Myers
# IT-140 Project Two
# The Legend of Tzevorg


# Greet the player and provide brief instruction
def intro():
    print(f"You have arrived at the entrance to the Old Fortress.\nThe fierce dragon Anvor'dris has stolen a"
          f' powerful ancient relic that controls the weather in the Kingdom of Tzevorg.\n\n'
          f'The kingdom has called upon you to help them retrieve it, but first you must collect six items:\n'
          f'\tThe Divine Sword, a Book of Spells, the Eltin Crystal,\n\tThe Unbreakable Shield, Magic Armor, '
          f"and the Key to Anvor'dris' Lair.\n\nEach room after the entrance will contain one of these items.\n\n"
          f'To move, type "go <direction>" (north, south, east, or west).\n'
          f'To collect an item, type "get <item>.\nType exit to give up.\n\n'
          f'Beware: All you need is the key to enter the dragon\'s lair, but that would be unwise.\n'
          f'The towering doors ahead of you lead to the Great Hall.')


# Print messages to player
def print_message(case):
    messages = {
        'Victory': f"You have entered the dragon's lair and used the items to slay Anvor'dris.\n"
                   f"Thank you for saving the Kingdom of Tzevorg!",
        'Loss': f"You have entered the dragon's lair unprepared. "
                f"You were barbecued and eaten by Anvor'dris.",
        'Keyless': "You need a key to enter the dragon's lair.",
        'Has Item': "You've already collected the item in this room.",
        'Quit': "You're giving up already? You've let the kingdom down. Goodbye."
    }

    if case in messages.keys():
        print(messages[case])
    else:
        print('Message not found. Uh-oh.')


def main():
    # The rooms of the fortress and their items
    rooms = {
        'Fortress Entrance': {
            'North': 'The Great Hall'
        },
        'The Great Hall': {
            'North': 'Throne Room',
            'East': 'Dungeon Keep',
            'West': 'The Whispering Library',
            'Item': 'The Divine Sword'
        },
        'The Whispering Library': {
            'North': "The Wizard's Decaying Apothecary",
            'East': 'The Great Hall',
            'Item': 'Book Of Spells'
        },
        "The Wizard's Decaying Apothecary": {
            'South': 'The Whispering Library',
            'East': 'Throne Room',
            'Item': 'Eltin Crystal'
        },
        'Throne Room': {
            'North': "Anvor'dris' Lair",
            'South': 'The Great Hall',
            'East': 'Armory',
            'West': "The Wizard's Decaying Apothecary",
            'Item': 'The Unbreakable Shield'
        },
        'Armory': {
            'South': 'Dungeon Keep',
            'West': 'Throne Room',
            'Item': 'Magic Armor'
        },
        'Dungeon Keep': {
            'North': 'Armory',
            'West': 'The Great Hall',
            'Item': "Key To Anvor'dris' Lair"
        },
        "Anvor'dris' Lair": {
            'Exit': 'Exit'
        }
    }

    # A list of cardinal directions for movement validation
    # These are used for custom error messaging
    cardinal_directions = ["North", "South", "East", "West"]

    # Set the "Great Hall" as the starting room
    current_room = rooms['Fortress Entrance']
    inventory = []

    intro()

    # Prompt the player for their first direction
    user_command = input('What is your first move? ')

    # Continuously loop until the player exits the game (using the exit command)
    # I've left this command in the code because it's my understanding that requiring
    # the exit keyboard shortcut is bad practice.
    while user_command.lower() != 'exit':
        # Split command and get direction
        if len(user_command.split()) > 1:
            user_command = user_command.split(maxsplit=1)[1]

        # Transform command to titlecase to match with a room's key
        # and, if the direction works in the current room, move that direction
        if user_command.title() in current_room.keys() and user_command.title() != 'Item':
            # Check if the player is entering the lair
            if current_room[user_command.title()] == "Anvor'dris' Lair":
                # Check if the key is in player inventory
                if "Key To Anvor'dris' Lair" in inventory:
                    # Check if they have every item. If they do they win.
                    if len(inventory) >= 6:
                        print_message('Victory')
                        exit()
                    # If they don't they lose.
                    else:
                        print_message('Loss')
                        exit()
                # Remind player they need a key to enter the lair.
                else:
                    print_message('Keyless')
            else:
                # Inform player of new location and set current room
                print(f'You have entered the {current_room[user_command.title()]}.')
                current_room = rooms[current_room[user_command.title()]]
                # If the player hasn't collected this room's item, hint at it.
                if current_room['Item'] not in inventory:
                    print(f"You see {current_room['Item']}.")
        # Backup bad input case
        elif user_command.title() not in current_room.keys() and user_command.title() not in current_room.values():
            if user_command.title() in cardinal_directions:
                print(f'You start to go {user_command.lower()} and see a wall. Just a plain wall. Not even a secret '
                      f'passage. Try again.')
            else:
                print(f'{user_command.lower()}? What is that?')
        # If not a direction, the player must be collecting an item.
        elif (user_command.title() not in cardinal_directions) \
              and (user_command.title() in current_room['Item']) or user_command.title() == 'Item':
            # If they've already gotten the item from this room, let them know.
            if current_room['Item'] in inventory:
                print_message('Has Item')
            # If they haven't, update their inventory and tell them.
            else:
                inventory.append(current_room['Item'])
                print(f'You have added {current_room["Item"]} to your inventory.')
        # Inform the player of the bad move.
        else:
            # Let the player know they tried to go somewhere they can't
            if user_command.title() in cardinal_directions:
                print(f'You start to go {user_command.lower()} and see a wall. Just a plain wall. Not even a secret '
                      f'passage. Try again.')
            else:
                print(f'{user_command.title()}? What is that?')

        # Show player their inventory and ask for next move.
        print(f"Inventory: {inventory}\n"
              f"{str('-' * 80)}")
        user_command = input('What is your next move? ')
    else:
        # Chide player for giving up on their quest
        print_message('Quit')


main()
