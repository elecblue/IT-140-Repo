# Nik Myers
# IT-140 | Module Six Milestone

# A dictionary for the simplified dragon text game
# The dictionary links a room to other rooms
rooms = {
    'Great Hall': {'South': 'Bedroom'},
    'Bedroom': {'North': 'Great Hall', 'East': 'Cellar'},
    'Cellar': {'West': 'Bedroom'}
}

# A list of cardinal directions for movement validation
# These are used for custom error messaging
cardinal_directions = ["North", "South", "East", "West"]

# Set the "Great Hall" as the starting room
current_room = rooms['Great Hall']

# Greet the player and provide brief instruction
print(f'Welcome to the Great Hall. Can you make it to the cellar?\n'
      f'To move, type "go <direction>" (north, south, east, or west). Type exit to give up.\n')

# Prompt the player for their first direction
user_command = input('Where will you go? ')

# Continuously loop until the player exits the game (using the exit command)
while user_command.lower() != 'exit':
    # Split command and get direction
    if len(user_command.split()) > 1:
        user_command = user_command.split(maxsplit=1)[1]

    # Transform command to titlecase to match with a room's key
    # and, if the direction works in the current room, move that direction
    if user_command.title() in current_room.keys():
        # Check if the player has entered the cellar to celebrate
        if current_room[user_command.title()] == 'Cellar':
            print('Huzzah! You made your way to the cellar and won... nothing.')
            current_room = rooms[current_room[user_command.title()]]
        else:
            # Inform player of new location and set current room
            print(f'You have entered the {current_room[user_command.title()]}.')
            current_room = rooms[current_room[user_command.title()]]
    else:
        # Let the player know they tried to go somewhere they can't
        if user_command.title() in cardinal_directions:
            print(f'You start to go {user_command.lower()} and see a wall. Just a plain wall. Not even a secret '
                  f'passage. Try again.')
        else:
            print(f'{user_command.lower()}? Do you know where you are going?')

    # Prompt the player for another direction
    user_command = input('Where will you go next? ')
else:
    # Chide player for giving up on their quest
    print('Giving up already? I hope you\'re proud.')
