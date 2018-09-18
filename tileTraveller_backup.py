# Hlynur Magnus Magnusson
# Hlynurm18@ru.is
# Assignment 8:  tileTraveller
# https://github.com/HlynurM/tileTraveller.git


# Setja upp fall sem vinnur ur key input
# Fall sem tekur key input og setur inn i mover(x,y)
# Fall sem athugar hvort veggir seu til stadar
# Fall sem prentar ut villuskilabod ef leid er lokud 
#               print("Not a valid direction")
# Setja upp fall sem init_fall() sem setur upp hluti i byrjun
# Fall sem keyrir adal luppu start() fall


# Algorithmi fyrir fyrsta hlutann

# Setja upp grid med tvofaldri for lykkju fyrir hnit x, y
#       x1, x2, x3, y1, y2, y3 = 1, 2, 3, 1, 2, 3
#       Tharf ad setja upp grid? Er nog ad tekka fyrir hverja hreyfingu hvort x, y se inni i grid moguleikum
# Setja inn upphafs punkt x1, y1
# Setja inn loka punkt x3, y1
# Skilgreina veggi
# Skilgreina leyfileg directions

# taka inn input um direction
# setja direction i lower()

# mover(direction)
# Ef nordur: y += 1, sudur: y -=1
# Ef austur: x += 1, vestur: -=1


# Setja upp
direction = 1
# Grid
x1, x2, x3, y1, y2, y3 = 1, 2, 3, 1, 2, 3
pos_x, pos_y = x1, y1
north = "(N)orth."
south = "(S)outh."
east = "(E)ast."
west = "(W est."
possible_dir = ''


while 1:

    # Setja upp oll tiles
    if pos_x == 1 and  pos_y == 1: possible_dir = 'n'; tile_11 = "(N)orth."
    elif pos_x == 1 and  pos_y == 2:possible_dir = 'nse'; tile_12 = "(N)orth or (E)ast or (S)outh.
    elif pos_x == 1 and  pos_y == 3:possible_dir = 'se'; tile_13
    elif pos_x == 2 and  pos_y == 1:possible_dir = 'n'; tile_21
    elif pos_x == 2 and  pos_y == 2:possible_dir = 'sw'; tile_22
    elif pos_x == 2 and  pos_y == 3:possible_dir = 'ew'; tile_23
    elif pos_x == 3 and  pos_y == 1:
        print("Victory!")
        break
    elif pos_x == 3 and  pos_y == 2:possible_dir = 'ns'; tile_32
    elif pos_x == 3 and  pos_y == 3:possible_dir = 'sw'; tile_33

    compass = north
    print("You can travel:", compass)
    direction = input("Direction: ").lower()

    #mover(direction):
    if (direction == "n") and ('n' in possible_dir):
        pos_y += 1
    elif (direction == "s" )and ('s' in possible_dir):
        pos_y -= 1
    elif (direction == "e") and ('e' in possible_dir):
        pos_x += 1
    elif (direction == "w") and ('w' in possible_dir):
        pos_x -= 1
    else:
        print("Not a valid direction")

    # #mover(direction):
    # if (direction == "n") and (pos_y < 3):
    #     pos_y += 1
    # elif (direction == "s" )and (1 < pos_y):
    #     pos_y -= 1
    # elif (direction == "e") and (pos_x < 3):
    #     pos_x += 1
    # elif (direction == "w") and (1 < pos_x):
    #     pos_x -= 1
    # else:
    #     print("Not a valid direction")
    
    # walls()



    print("Debug Log: Loc:", pos_x, pos_y, "Direction: ", direction)
    # victory(x, y):
    if pos_x == x3 and pos_y == y1:
        print("Victory!")
        break
