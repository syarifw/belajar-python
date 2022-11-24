def turn_right():
    turn_left()
    turn_left()
    turn_left()

def custom_move():
    turn_left()
    move()
    turn_right()
    move()
    turn_right()
    move()
    turn_left()

while at_goal() != True:
    if front_is_clear() == True:
        move()
    if wall_in_front() == True:
        custom_move()