# Hlynur Magnus Magnusson
# Hlynurm18@ru.is
# Assignment 8:  tileTraveller
# https://github.com/HlynurM/tileTraveller.git

# BYRJUNAR GILDI
pos_x, pos_y = 1, 1
n, s, e, w = 1, -1, 1, -1 

# Tekur inn x, y og skilar ut mogulegar leidir
def current_tile(x_hnit, y_hnit):
    """Skilar ut mogulegar attir midad vid nuverandi hnit; 
    direction_map, possible_input_key"""
    victory = False
    if x_hnit == 1 and y_hnit == 1:     # 1,1
        direction_map = "(N)orth."
        possible_input_key = 'n'
    elif x_hnit == 1 and y_hnit == 2:   # 1,2
        direction_map = "(N)orth or (E)ast or (S)outh."
        possible_input_key = 'nes'
    elif x_hnit == 1 and y_hnit == 3:   # 1,3
        direction_map = "(E)ast or (S)outh."
        possible_input_key = 'es'
    elif x_hnit == 2 and y_hnit == 1:   # 2,1
        direction_map = "(N)orth."
        possible_input_key = 'n'
    elif x_hnit == 2 and y_hnit == 2:   # 2,2
        direction_map = "(S)outh or (W)est."
        possible_input_key = 'sw'
    elif x_hnit == 2 and y_hnit == 3:   # 2,3
        direction_map = "(E)ast or (W)est."
        possible_input_key = 'ew'
    elif x_hnit == 3 and y_hnit == 1:   # 3,1 Victory
        direction_map = "(N)orth."
        possible_input_key = 'n'
        victory = True
    elif x_hnit == 3 and y_hnit == 2:   # 3,2
        direction_map = "(N)orth or (S)outh."
        possible_input_key = 'ns'
    elif x_hnit == 3 and y_hnit == 3:   # 3,3
        direction_map = "(S)outh or (W)est."
        possible_input_key = 'sw'
    return direction_map, possible_input_key, victory

def dir_error():
    """Calls out invalid moves"""
    print("Not a valid direction!")

def mover(my_dir, valid_direction, x, y):
    """Moves player. Takes in: 
    Key input, valid directions and current x and y position"""
    if (my_dir in valid_direction):
        if my_dir == 'n' or my_dir == 's':
            y += eval(my_dir)
        else:
            x += eval(my_dir)
    else:
        # If move not valid, call out the error!
        dir_error()
    return x, y

def input_key():
    """Returns keystroke input: lower case"""
    direction = input("Direction: ").lower()
    return direction

def travel_guide(map, victory):
    """Prints out possible directions from current tile"""
    if victory != True:
        print("You can travel: " + map)
    else:
        print("Victory!")

# Start the dungeon crawler!
while 1:
    # What tile is player on currently
    direction_map, possible_key_input, victory = current_tile(pos_x, pos_y)

    # Where can I travel
    travel_guide(direction_map, victory)
    if victory == True:
        break

    # What is my direction choice
    direction = input_key()

    # Update x, y coordinates to move character based on possible moves.
    pos_x, pos_y = mover(direction, possible_key_input, pos_x, pos_y)