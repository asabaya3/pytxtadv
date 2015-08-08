def start_game(player, room, intro = None):
    print(intro) if intro else None
    player.location = room
    room.enter(player)
    
    global running
    running = True
    
    update_list.append(player)
    game_loop(player)

def end_game():
    global running
    running = False

def game_loop(player):
    while running:
        # First word is the command, rest are arguments
        line = input('>').split(maxsplit = 1)
        command = line[0]
        args_string = line[1] if len(line) == 2 else None
        if command in commands:
            if commands[command](player, args_string):
                update_game()
        else:
            print(command + " is not a valid command")

def update_game():
    for thing in update_list:
        thing.act()
    for thing in update_list:
        thing.update()

def register_command(name, function):
    commands[name] = function
    return function

def move(player, arg_string):
    room, direction = player.location.exit(player, arg_string)
    if room:
        player.location = room
        room.enter(player, direction)

def move_n(player, arg_string):
    move(player, 'north')

def move_s(player, arg_string):
    move(player, 'south')

def move_e(player, arg_string):
    move(player, 'east')

def move_w(player, arg_string):
    move(player, 'west')

def move_u(player, arg_string):
    move(player, 'up')

def move_d(player, arg_string):
    move(player, 'down')

def move_i(player, arg_string):
    move(player, 'in')

def move_o(player, arg_string):
    move(player, 'out')

def examine(player, arg_string):
    if not arg_string:
        target = player.location
    if not target:
        target = player.location.check_actors(arg_string)
    if not target:
        target = player.location.check_items(arg_string)
    if not target:
        target = player.location.check_room(arg_string)
    if target:
        target.examine()
    else:
        print(arg_string + " not found")

def inventory(player, arg_string):
    print(player.inventory)

def talk(player, arg_string):
    args = arg_string.split(maxsplit = 1)
    if args[0] != 'to':
        print("Syntax is 'talk to <person>'")
    else:
        actor = player.location.check_actors(args[1])
        if actor:
            actor.talk()

def use(player, arg_string):
    args = arg_string.split(" on ")
    item_name = args[0]
    target = args[1] if len(args) == 2 else player
    item = player.check_inventory(item_name)
    if not item:
        item = player.location.check_items(item_name)
    if item:
        item.use(target)
    else:
        print(item_name + " not found")

def equip(player, arg_string):
    item = player.check_inventory(arg_string)
    if item:
        item.equip(player)
    else:
        print(item_name + " not in inventory")

def unequip(player, arg_string):
    item = player.check_inventory(arg_string)
    if item:
        item.unequip(player)
    else:
        print(item_name + " not in inventory")

def take(player, arg_string):
    item = player.location.check_items(arg_string)
    if item:
        player.location.take(item, player)
    else:
        print(item_name + " not found")

def drop(player, arg_string):
    item = player.check_inventory(arg_string)
    if item:
        player.location.drop(item, player)
    else:
        print(item_name + " not in inventory")

def wear(player, arg_string):
    item = player.check_inventory(arg_string)
    if item:
        item.wear(target)
    else:
        print(item_name + " not in inventory")

def remove(player, arg_string):
    item = player.check_inventory(arg_string)
    if item:
        item.remove(target)
    else:
        print(item_name + " not in inventory")

def open(player, arg_string):
    item = player.check_inventory(arg_string)
    if not item:
        item = player.location.check_items(arg_string)
    if item:
        item.open()
    else:
        print(arg_string + " not found")

def close(player, arg_string):
    item = player.check_inventory(arg_string)
    if not item:
        item = player.location.check_items(arg_string)
    if item:
        item.close()
    else:
        print(arg_string + " not found")

running = False
update_list = []

commands = {
    'move' : move,
    'n' : move_n,
    's' : move_s,
    'e' : move_e,
    'w' : move_w,
    'in' : move_i,
    'out' : move_o,
    'up' : move_u,
    'down' : move_d,
    'examine' : examine,
    'x' : examine,
    'inventory' : inventory,
    'i' : inventory,
    'talk' : talk,
    'use' : use,
    'equip' : equip,
    'unequip' : unequip,
    'wear' : wear,
    'remove' : remove,
    'take' : take,
    'drop' : drop,
    'open' : open,
    'close' : close,
    }

