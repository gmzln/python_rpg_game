from timer import start_timer
from displayText import show_game_over, show_game_win, show_monster_is_defeated
import threading

inventory = []
stop_input = False 
monster_is_defeated = False

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
                 'west' : 'Dining Room',
                 'north' : 'Laboratory',
                 'item' : 'bookoflife'
                 },
    'Office' : { 'east' : 'Laboratory',
                'west' : 'Library',
                'item' : 'monster'
                },
    'Laboratory' : {'south': 'Library',
                    'west' : 'Office',
                    'item' : 'beamomat'
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
    print('--------------------------------')
    print('Current status')
    print('--------------------------------')
    print('You are in the ' + currentRoom)
    #print the current inventory
    print('Inventory: ' + str(inventory))
    #print an item if there is one
    if 'item' in rooms[currentRoom]:
        print('You see a ' + rooms[currentRoom]['item'])
    print('--------------------------------')

# defeating the monster
def get_user_input(event):
    global stop_input, monster_is_defeated
    while not stop_input and not monster_is_defeated:
            move = input('> ').lower().split()
            if move[0] == 'throw' and move[1] == 'potion':
                inventory.remove('potion')
                show_monster_is_defeated()
                del rooms[currentRoom]['item']
                timer.cancel()
                monster_is_defeated = True
            elif timer.is_alive():
                    print('invalid input. Try again!')
            else:
                print('Donn\'t be sad. You can try again!')
                return
    return

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
    if move[0] == 'get' :
        if 'item' in rooms[currentRoom] and move[1] in rooms[currentRoom]['item']:
            inventory += [move[1]]
            print(move[1] + ' got!')
            del rooms[currentRoom]['item']
        else:
            print('Can\'t get ' + move[1] + '!')

   # defeat the monster
    if 'item' in rooms[currentRoom] and rooms[currentRoom]['item'] == 'monster':
        if 'potion' in inventory:
            print('A monster is here! You have 10 seconds to throw the potion!')

            timer, event = start_timer(10)
            input_thread = threading.Thread(target=get_user_input, args=(event,))
            input_thread.start()

            timer.join()

            # input thread && time thread
            if event.is_set() and monster_is_defeated is False:
                show_game_over()
                print('You ran out of time! Type [exit]')
                stop_input = True
                timer.cancel()
                break
        else:
            show_game_over()
            print('A monster has got you... GAME OVER! Come back next time with the potion!')
            break

    # winning condition
    if (currentRoom == 'Garden' and 'key' in inventory and 'potion') or \
        (currentRoom == 'Laboratory' and 'bookoflife' in inventory and 'beamomat') in inventory:
         show_game_win()
         break
    if move[0] == 'exit':
         break