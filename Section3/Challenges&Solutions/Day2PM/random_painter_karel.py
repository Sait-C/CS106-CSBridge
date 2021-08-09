from karel.stanfordkarel import *

"""
File: random_painter_karel.py
------------------------------
Your job is to paint random squares all over the world!
Pick two colors and choose randomly between them for each
square.
"""
run = True

def paint_world():
    global run
    while run:
        paint_current_row_to_right()
        move_up_from_right()
        paint_current_row_to_left()
        move_up_from_left()

def turn_right():
    for i in range(3):
        turn_left()

def paint_random():
    if random(0.5):
        paint_corner(BLACK)
    else:
        paint_corner(RED)

def paint_current_row_to_right():
    while front_is_clear():
        paint_random()
        move()
    paint_random()

def move_up_from_right():
    global run
    if check_left():
        turn_left()
        move()
        turn_left()
    else:
        run = False

def move_up_from_left():
    global run
    if check_right():
        turn_right()
        move()
        turn_right()
    else:
        run = False

def check_right():
    return right_is_clear()

def check_left():
    return left_is_clear()

def paint_current_row_to_left():
    while front_is_clear():
        paint_random()
        move()
    paint_random()

def main():
    """
    You should write your code to make Karel do its task in
    this function. Make sure to delete the 'pass' line before
    starting to write your own code. You should also delete this
    comment and replace it with a better, more descriptive one.
    """
    paint_world()


# There is no need to edit code beyond this point

if __name__ == "__main__":
    run_karel_program()
