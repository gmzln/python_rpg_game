inventory = []

rooms = {
    'Hall' : {
        'south' : 'Kitchen'
    },
    'Kitchen' : {
        'north' : 'Hall'
    }
}

currentRoom = 'Hall'

def showInstructions():
    #print a main menu and the commands
    print('''
    Welcome to your own RPG Game
    ----------------------------

    Get to the Garden with a key and potion.
    Avoid the monsters!

    Commands:
        go [direction]
        get [item]
    ''')

def showStatus():
    #print the players current status
    print('--------------------------------')
    print('You are in the' + currentRoom)
    #print the current inventory
    print('Inventory: ' + str(inventory))
    #print an item if there is one
    if 'item' in rooms[currentRoom]:
        print('You see a ' + rooms[currentRoom]['item'])
    print('--------------------------------')


showInstructions()
while True:
    showStatus()
    move = ''
    while move == '':
            move = input('>')
    move = move.lower().split()
    if move[0] == 'exit':
         break
    if move[0] == 'go':
         if move[1] in rooms[currentRoom]:
              currentRoom = rooms[currentRoom][move[1]]
    else:
        print('You cant go that way!')