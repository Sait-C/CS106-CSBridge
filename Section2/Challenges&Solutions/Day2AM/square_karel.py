from karel.stanfordkarel import *

"""
File: square_karel.py
------------------------------
Your job is to write a program that lets Karel place an outline
of beepers in a square world. You should make sure that
your program works for all of the sample square worlds,
like 8x8, 5x5, 3x3, 2x2, and 1x1.
"""


def main():
    """
    You should write your code to make Karel do its task in
    this function. Make sure to delete the 'pass' line before
    starting to write your own code. You should also delete this
    comment and replace it with a better, more descriptive one.
    """
    for i in range(4):
        while front_is_clear():
            put_beeper()
            move()
        turn_left()


# There is no need to edit code beyond this point

if __name__ == "__main__":
    run_karel_program()
