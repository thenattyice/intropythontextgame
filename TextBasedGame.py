#Name: Nathan Kimborowicz

#Function showing the goal of the game and move commands
def show_instructions():
    # Print a main menu and the commands
    print("Medieval Text Adventure Game")
    print("Collect 6 items to win the game, or be eaten by the monster.")
    print("Move commands: move South, move North, move East, move West")
    print("Add to Inventory: get 'item name'")
    print()

#Holds the user's current room. User starts in King's Hall
current_room = 'King\'s Hall'

#List to hold the player's items
inventory = []

# Dictionary of all rooms, their directions and items
rooms = {
    'King\'s Hall': {
            'directions': {'East': 'Armory', 'West': 'Stables', 'North': 'Kitchen', 'South': 'Apothecary'},
            'item': None
    },
    'Apothecary': {
        'directions': {'North': 'King\'s Hall', 'East': 'Lookout Tower'},
        'item': 'Potion Pouch'
    },
    'Lookout Tower': {
        'directions': {'West': 'Apothecary'},
        'item': 'Bow'
    },
    'Armory': {
        'directions': {'West': 'King\'s Hall', 'North': 'Guard Barracks'},
        'item': 'Sword'
    },
    'Guard Barracks': {
        'directions': {'South': 'Armory'},
        'item': 'Armor Set'
    },
    'Stables': {
        'directions': {'East': 'King\'s Hall'},
        'item': 'Shield'
    },
    'Kitchen': {
        'directions': {'South': 'King\'s Hall', 'East': 'Dungeon'},
        'item': 'Quiver'
    },
    'Dungeon': {
        'directions': {'West': 'Kitchen'},
        'item': 'Monster'
    }
}

def main():

    #List of valid directions for user input in game commands
    valid_directions = {'North', 'South', 'East', 'West'}

    #Function to display user's current room
    def status():
        if rooms[current_room]['item'] == None:
            print('You are in the', current_room)
            print(f'Inventory: {inventory}')
            print('----------------------')
        else:
            print('You are in the', current_room)
            print(f'Inventory: {inventory}')
            print(f'You see a {rooms[current_room]['item']}')
            print('----------------------')

    #Function that outlines the primary game commands
    def commands():
        #I added maxsplit to allow for anything after get to be kept as one item to allow for items like Potion Pouch to be accepted
        move = input('Enter your move: ').strip().split(maxsplit=1)

        #Confirm that the command is valid and set the direction. Added capitalize to make it case-insensetive for better user-experience
        if len(move) == 2 and move[0] == 'move' and move[1].capitalize() in valid_directions:
            direction = move[1].capitalize()
            #Validate that the direction is in nested dictionary for the current room
            global current_room
            if direction in rooms[current_room]['directions']:
                current_room = rooms[current_room]['directions'][direction]
                print('You have moved to the', current_room)
            else:
                print('You cannot move in that direction')
        #Validation for get command
        elif len(move) == 2 and move[0] == 'get':
            room_item = rooms[current_room]['item']
            if rooms[current_room]['item'] is not None and rooms[current_room]['item'] not in inventory:
                #Validating that the item entered matches the item in the dictionary. Added lower to make it case-insensetive for better user-experience
                if move[1].lower() == room_item.lower():
                    print(f'You found a {room_item} and have picked it up!')
                    inventory.append(room_item)
                    rooms[current_room]['item'] = None
                else:
                    print('Please entr a valid item to pick up or make sure that there is an item in the room.')
            elif room_item in inventory:
                print('You have already collected the item from this room.')
            else:
                print('There is nothing to collect in this room.')
        #Invalid command message based on above validation
        else:
            print('Invalid command. Must start with "move" and be followed by North, South, East, or West.')

    #Calling the nested functions to fire off when main is called in the game loop
    status()
    commands()

#Show the instructions before the gameplay loop starts, that way they don't keep popping up
show_instructions()
#Game loop
while True:
    main()
    if current_room == 'Dungeon':
        if len(inventory) == 6:
            print('Congratulations! You have collected all items and defeated the monster!')
            print('Thanks for playing the game. Hope you enjoyed it.')
            break
        else:
            print('NOM NOM...GAME OVER!')
            print('Thanks for playing the game. Hope you enjoyed it.')
            break