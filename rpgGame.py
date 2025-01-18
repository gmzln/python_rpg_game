import time

inventory = []

rooms = {
    'Hall' : {
        'south' : 'Kitchen',
        'east' : 'Dining Room',
        'item' : 'key',
    },
    'Kitchen' : {
        'north' : 'Hall',
        'item' : 'monster',
    },
    'Dining Room' : { 'west' : 'Hall',
                     'south' : 'Garden',
                     'east' : 'Library',
                     'item' : 'potion',
                     },
    'Garden' : { 'north' : 'Dining Room'},
    'Library' : { 'east' : 'Office',
                 'west' : 'Dining Rooon',
                 'north' : 'Laboratory',
                 'item' : 'BookOfLife'
                 },
    'Office' : { 'east' : 'Laboratory',
                'west' : 'Library',
                'item' : 'monster'
                },
    'Laboratory' : {'south': 'Library',
                    'west' : 'Office',
                    'item' : 'Beam-O-Mat'
                    },
}

currentRoom = 'Hall'

def showInstructions():
    #print a main menu and the commands
    print('''
    Welcome to the RPG Game
    ----------------------------

    How to win:
    Get to the Garden with a key and potion or
    to the Laboratory with the BookOfLife 
    and Beam-O-Mat.
    
    Avoid the monsters or defeat them!

    Commands:
        go [direction]
        get [item]
        throw [potion]
    ----------------------------
    ''')

def showStatus():
    #print the players current status
    print('Current status')
    print('--------------------------------')
    print('You are in the ' + currentRoom)
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
                print('You can\'t go that way!')
    # picking up items
    if move[0] == 'get':
            if 'item' in rooms[currentRoom] and move[1] in rooms[currentRoom]['item']:
                inventory += [move[1]]
                print(move[1] + ' got!')
                del rooms[currentRoom]['item']
            else:
                print('Can\'t get ' + move[1] + '!')
    # defeat the monster
    if move[0] == 'throw':
            if 'item' in rooms[currentRoom] and rooms[currentRoom]['item'] == 'monster':
                if 'potion' in inventory:
                    print('A monster is here! You have 10 seconds to throw the potion!')
                    start_time = time.time()
                    while time.time() - start_time < 10:
                        move = input('> ').lower().split()
                        if move[0] == 'throw' and move[1] == 'potion':
                            inventory.remove('potion')
                            print('You threw the potion! The monster is defeated!')
                            del rooms[currentRoom]['item']
                            break
                        else:
                            print('You ran out of time! The monster got you... GAME OVER!')
                            break   
            else:
                print('A monster has got you... GAME OVER!')
                break
    if 'item' in rooms[currentRoom] and 'monster' in rooms[currentRoom]['item']:
         print('A monster has got you... GAME OVER!')
         break
    # winning logic
    if (currentRoom == 'Garden' and 'key' in inventory and 'potion') or \
        (currentRoom == 'Laboratory' and 'BookOfLife' in inventory and 'Beam-O-Mat') in inventory:
         print('You escaped the house... YOU WIN!')
         break
    if move[0] == 'exit':
         break