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
    
#dir mover(direction):

    if (direction == 'n') and ('n' in valid_direction):
        char_y += 1
    elif (direction == 's') and ('s' in valid_direction):
        char_y -= 1
    elif (direction == 'e') and ('e' in valid_direction):
        char_x += 1
    elif (direction == 'w') and ('w' in valid_direction):
        char_x -= 1
    else:
        print("Not a valid direction!")
        travel_agree = 0

#dir veggir(char_x, char_y):

    if char_x == 1 and char_y == 1: path = room1_1; valid_direction = 'n'
    elif char_x == 1 and char_y == 2: path = room1_2; valid_direction = 'nes'
    elif char_x == 1 and char_y == 3: path = room1_3; valid_direction = 'es'
    elif char_x == 2 and char_y == 1: path = room2_1; valid_direction = 'n'
    elif char_x == 2 and char_y == 2: path = room2_2; valid_direction = 'ws'
    elif char_x == 2 and char_y == 3: path = room2_3; valid_direction = 'we'
    elif char_x == 3 and char_y == 1: path = room3_1; print("Victory!"); break
    elif char_x == 3 and char_y == 2: path = room3_2; valid_direction = 'ns'
    elif char_x == 3 and char_y == 3: path = room3_3; valid_direction = 'ws'
    
# for x,y in :
#     if char_x == x and char_y == y: 
#         path = what_room(x,y)
#         valid_direction = 

    # if 'e' in walls:
    #     char_x -= 1
    #     print("Not a valid direction!")
    

    # print("Current location",char_x, char_y)