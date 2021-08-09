from karel.stanfordkarel import *

"""
File: stripe_karel.py
------------------------------
At present, this file does nothing. Your job is to place
a line of beepers on every odd row. You can assume that there
are an odd number of rows in the world, and you should make sure
that your program works for all of the sample stripe worlds.
"""
run = True

def move_to_end():
    while front_is_clear():
        if not beepers_present():
            put_beeper()
        move()

def go_back():
    turn_around()
    move_to_end()

def turn_around():
    turn_left()
    turn_left()

def move_next_odd_row():
    global run
    turn_right()
    for i in range(2): #for odd rows
        if front_is_clear():
            move()
        else:
            run = False
            break
    turn_right()

def turn_right():
    for i in range(3):
        turn_left()

def main():
    """
    You should write your code to make Karel do its task in
    this function. Make sure to delete the 'pass' line before
    starting to write your own code. You should also delete this
    comment and replace it with a better, more descriptive one.
    """
    global run
    while run:
        move_to_end()
        go_back()
        move_next_odd_row()


# There is no need to edit code beyond this point

if __name__ == "__main__":
    run_karel_program()
