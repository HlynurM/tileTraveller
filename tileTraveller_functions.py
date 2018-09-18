""" með tvo int: char_x og char_y sem tilgreinir hvar character er
    if( x og y) þá hvað: m.v. aðstæður á hverjum stað fyrir sig
    þegar character nær inn í 3.1 þá victory
    í hverri loopu skrifast út status update, you can travel: 
    (set upp git)
    (N)orth
    (S)outh
    (W)est
    (E)ast
    """

#Upphafsstaða - í room1_1
char_x, char_y = 1, 1
path = ""
valid_direction = 'n'

# foll
def mover(my_dir, x, y):
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
        travel_agree = 0
    return char_x, char_y

# dir_compass(x,y):
#     if char_x == x and char_y == y: 
#         path = what_room(x,y)
#         valid_direction = room_dir(x,y)

#  what_room():
    

# Rooms
room1_1 = "(N)orth."
room1_2 = "(N)orth or (E)ast or (S)outh." 
room1_3 = "(E)ast or (S)outh."
room2_1 = "(N)orth."
room2_2 = "(S)outh or (W)est."
room2_3 = "(E)ast or (W)est."
room3_1 = "(N)orth."
room3_2 = "(N)orth or (S)outh."
room3_3 = "(S)outh or (W)est."
path = room1_1

travel_agree = 1

while 1:
    
    if travel_agree == 1:
        print("You can travel: " + path)

    path = ''
    direction = input("Direction: ").lower()
    travel_agree = 1
    
    char_x, char_y = mover(direction, char_x, char_y)

    if char_x == 1 and char_y == 1: path = room1_1; valid_direction = 'n'
    elif char_x == 1 and char_y == 2: path = room1_2; valid_ndirection = 'nes'
    elif char_x == 1 and char_y == 3: path = room1_3; valid_direction = 'es'
    elif char_x == 2 and char_y == 1: path = room2_1; valid_direction = 'n'
    elif char_x == 2 and char_y == 2: path = room2_2; valid_direction = 'ws'
    elif char_x == 2 and char_y == 3: path = room2_3; valid_direction = 'we'
    elif char_x == 3 and char_y == 1: path = room3_1; print("Victory!"); break
    elif char_x == 3 and char_y == 2: path = room3_2; valid_direction = 'ns'
    elif char_x == 3 and char_y == 3: path = room3_3; valid_direction = 'ws'


