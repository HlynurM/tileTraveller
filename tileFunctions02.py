# Hlynur Magnus Magnusson
# Hlynurm18@ru.is
# Assignment 8:  tileTraveller
# https://github.com/HlynurM/tileTraveller.git

# FASTAR

# BYRJUNAR GILDI
pos_x, pos_y = 1, 1

# Athuga hvort styttri leid se ad innleida current_tile. Hvort loopa eda auka fall inni 
# fallinu virki betur. Eda ekki!
def current_tile(x_hnit, y_hnit):
    """Skilar ut mogulegar attir midad vid nuverandi hnit; compass, possible moves"""
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
        victory = True
        direction_map = "(N)orth."
        possible_input_key = 'n'
    elif x_hnit == 3 and y_hnit == 2:   # 3,2
        direction_map = "(N)orth or (S)outh."
        possible_input_key = 'ns'
    elif x_hnit == 3 and y_hnit == 3:   # 3,3
        direction_map = "(S)outh or (W)est."
        possible_input_key = 'sw'
    else:
        dir_error()
    return direction_map, possible_input_key, victory

def dir_error():
    print("Not a valid direction!")

def mover(my_dir, x, y, valid_direction):
    if ((my_dir == 'n') and ('n' in valid_direction)):    
        y += 1
    elif ((my_dir == 's') and ('s' in valid_direction)):
        y -= 1
    elif ((my_dir == 'e') and ('e' in valid_direction)):
        x += 1
    elif ((my_dir == 'w') and ('w' in valid_direction)):
        x -= 1
    else:
        print("Not a valid direction!")
    return x, y

def input_key():
    direction = input("Direction: ").lower()
    return direction

# Starta leik
while 1:
    direction_map, possible_key_input, victory = current_tile(pos_x, pos_y)
    print("Map:", direction_map, "key:", possible_key_input, "victory", victory)

    print("You can travel: " + direction_map)
    the_key = input_key()
    mover(the_key, pos_x, pos_y, possible_key_input)


    # # Debug /////////////////////////////////////////////////////////////////////////////////////////////
    # print("Compass: ", direction_map, "Valid path key: ", possible_key_input, "Victory:" ,victory)

    # if victory == False:
    #     print("Victory!")
    #     break

    where_am_i(x, y)            # 3 x 3 tile dungeon

    tell_me_open_paths(x, y)    # N S E W

    move_me()                   # update x, y based on open N S E W

