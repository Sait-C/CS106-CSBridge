from karel.stanfordkarel import *

"""
File: hurdle_jumper.py
------------------------
Karel runs a set of hurdles that are 9 avenues long.
Hurdles are of arbitrary height and placement.
"""


def main():
    """
    To run a race that is 9 avenues long, we need
    to move forward or jump hurdles 8 times.
    """
    for i in range(8):
        if front_is_clear():
            move()
        else:
            jump_hurdle()


def jump_hurdle():
    """
    Karel jumps over one hurdle of arbitrary height.
    Pre-condition:  Karel is facing east next to a hurdle.
    Post-condition: Karel is facing east at the bottom of
                   the other side of the hurdle.
    """
    ascend_hurdle()
    move()
    descend_hurdle()


def ascend_hurdle():
    """
    Karel climbs up the side of a hurdle.
    Pre-condition:  Karel is facing east at the bottom of
                   a hurdle.
    Post-condition: Karel is facing east above and immediately
                   before a hurdle.
    """
    turn_left()
    while right_is_blocked():
        move()
    turn_right()


def descend_hurdle():
    """
    Karel climbs down the side of a hurdle.
    Pre-condition: Karel is facing east above and
                  immediately after a hurdle.
    Post-condition: Karel is facing east at the bottom of
                   the hurdle.
    """
    turn_right()
    move_to_wall()
    turn_left()


def move_to_wall():
    """
    Karel moves until it reaches a wall.
    Pre-condition:  none
    Post-condition: Karel is facing a wall in whichever
                   direction Karel was facing previously.
    """
    while front_is_clear():
        move()


def turn_right():
    """
    Karel turns 90 degrees to the right.
    Pre-condition: none
    Post-condition: Karel is facing 90 degrees right of where
                    it was originally facing.
    """
    for i in range(3):
        turn_left()


# There is no need to edit code beyond this point

if __name__ == "__main__":
    run_karel_program()
