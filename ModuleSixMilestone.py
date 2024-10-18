#Name: Nathan Kimborowicz

#A dictionary for the simplified dragon text game
#The dictionary links a room to other rooms.
rooms = {
        'Great Hall': {'South': 'Bedroom'},
        'Bedroom': {'North': 'Great Hall', 'East': 'Cellar'},
        'Cellar': {'West': 'Bedroom'}
    }

#Holds the user's current room. USer starts in Great Hall
current_room = 'Great Hall'

#List of valid directions for user input in game commands
valid_directions = {'North', 'South', 'East', 'West'}

#Function to display user's current room
def room_check():
    print('You are in the', current_room)

#Function to prompt the user and move the user to a new room
def change_rooms():
    global current_room
    move = input('Enter a direction to move in (North, South, East, or West):' ).strip()

    # Allows current_room to be exit so that player can exit the game before move becomes a list
    if move == 'exit':
        current_room = 'exit'
        return

    #Seperate move into a list for validaton to be compelted
    move = move.split()

    #Validate that the command is valid and set the direction
    if len(move) == 2 and move[0] == 'move' and move[1] in valid_directions:
        direction = move[1]
        #Validate that the direction is in nested dictionary for the current room
        if direction in rooms[current_room]:
            current_room = rooms[current_room][direction]
            print('You have moved to the ', current_room)
        else:
            print('You cannot move in that direction')
    #Invalid command message based on above validation
    else:
        print('Invalid command. Must start with "move" and be followed by North, South, East, or West. Player may also type "exit" to exit the game')

#Gameplay loop
while True:
    # Allows user to exit the game loop
    if current_room == 'exit':
        print('Exiting the game.')
        break
    room_check()
    change_rooms()

