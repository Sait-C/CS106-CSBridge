from karel.stanfordkarel import *

"""
File: sweeper.py
------------------------
This program has Karel clean up any beepers to its right.
"""


def main():
    """
    When you start your program, this code will be executed.
    """
    while front_is_clear():
        move()
        if beepers_present():
            pick_beeper()


# There is no need to edit code beyond this point

if __name__ == "__main__":
    run_karel_program()
