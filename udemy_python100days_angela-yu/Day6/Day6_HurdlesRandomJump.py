# Syarif Solving

def turn_right():
    turn_left()
    turn_left()
    turn_left()

def jump():
    turn_left()
    move()
    indeks=0
    while wall_on_right() == True:
        move()
        indeks+=1
    turn_right()
    move()
    turn_right()
    move()
    while indeks >0:
        move()
        indeks-=1
    turn_left()

while at_goal() != True:
    if front_is_clear() == True:
        move()
    if wall_in_front() == True:
        jump()

# Angela Yu Solving :

def turn_right():
    turn_left()
    turn_left()
    turn_left()

def jump():
    turn_left()
    while wall_on_right():
        move()
    turn_right()
    move()
    turn_right()
    while front_is_clear():
        move()
    turn_left()

while at_goal() != True:
    if front_is_clear():
        move()
    if wall_in_front():
        jump()