#Name: Nathan Kimborowicz

#Function showing the goal of the game and move commands
def show_instructions():
   #print a main menu and the commands
   print("Medieval Text Adventure Game")
   print("Collect 6 items to win the game, or be eaten by the monster.")
   print("Move commands: move South, move North, move East, move West")
   print("Add to Inventory: get 'item name'")
   print()

def main():
    #Dictionary of all rooms, their directions and items
    rooms = {
        'King’s Hall': {
            'directions': {'East': 'Armory', 'West': 'Stables', 'North': 'Kitchen', 'South': 'Apothecary'},
            'item': None
        },
        'Apothecary': {
            'directions': {'North': 'King’s Hall', 'East': 'Lookout Tower'},
            'item': 'Potion Pouch'
        },
        'Lookout Tower': {
            'directions': {'West': 'Apothecary'},
            'item': 'Bow'
        },
        'Armory': {
            'directions': {'West': 'King’s Hall', 'North': 'Guard Barracks'},
            'item': 'Sword'
        },
        'Guard Barracks': {
            'directions': {'South': 'Armory'},
            'item': 'Armor'
        },
        'Stables': {
            'directions': {'East': 'King’s Hall'},
            'item': 'Shield'
        },
        'Kitchen': {
            'directions': {'South': 'King’s Hall', 'East': 'Dungeon'},
            'item': 'Quiver'
        },
        'Dungeon': {
            'directions': {'West': 'Kitchen'},
            'item': 'Monster'
        }
    }

    #List to hold the player's items
    inventory = []

    #Holds the user's current room. USer starts in Great Hall
    current_room = 'King’s Hall'

    #List of valid directions for user input in game commands
    valid_directions = {'North', 'South', 'East', 'West'}

    #Function to display user's current room
    def status():
        print('You are in the', current_room)
        print(f'Inventory: {inventory}')
        #Add an if/then for seeing an item in the room
        print('----------------------')

    #Function that outlines the primary game commands
    def commands(current_room):
        move = input('Enter your move: ' ).strip().split()

        #Confirm that the command is valid and set the direction
        if len(move) == 2 and move[0] == 'move' and move[1] in valid_directions:
            direction = move[1]
            #Validate that the direction is in nested dictionary for the current room
            if direction in rooms[current_room][directions]:
                current_room = rooms[current_room][directions]
                print('You have moved to the ', current_room)
            else:
                print('You cannot move in that direction')
        #Validation for get command
        elif len(move) == 2 and move[0] == 'get' and move[1] in rooms[current_room]['item']:
            room_item = rooms[current_room]['item']
            if room_item in inventory:
                print('You have already collected the item from this room.')
            else:
                print(f'You found a {room_item} and have picked it up!')
                inventory.append(room_item)
        #Invalid command message based on above validation
        else:
            print('Invalid command. Must start with "move" and be followed by North, South, East, or West. Player may also type "exit" to exit the game')
        return current_room

    #Calling the nested functions to fire off when main is called in the game loop
    status()
    current_room = commands(current_room)
    return current_room

#Game loop
while True:
    # Show the instructions before the gameplay loop starts, that way they don't keep popping up
    show_instructions()
    current_room = main()
