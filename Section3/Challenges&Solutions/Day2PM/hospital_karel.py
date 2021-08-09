from karel.stanfordkarel import *

"""
File: hospital_karel.py
------------------------------
Your job is to help Karel build new hospitals in
the places marked by each beeper in the original world.
"""

def turn_right():
    for i in range(3):
        turn_left()

def build_column():
    for i in range(2):
        move()
        put_beeper()

def build_hospital():
    turn_left()
    build_column()
    turn_right()
    move()
    turn_right()
    put_beeper()
    build_column()
    turn_left()

def main():
    """
    You should write your code to make Karel do its task in
    this function. Make sure to delete the 'pass' line before
    starting to write your own code. You should also delete this
    comment and replace it with a better, more descriptive one.
    """
    while front_is_clear(): # while we're not at the end of the world
        if beepers_present():
            build_hospital()
        if front_is_clear():
            move()


# There is no need to edit code beyond this point

if __name__ == "__main__":
    run_karel_program()