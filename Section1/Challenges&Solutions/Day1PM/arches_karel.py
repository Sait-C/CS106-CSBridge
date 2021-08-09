from karel.stanfordkarel import *

"""
File: arches_karel.py
------------------------------
When you finish writing code in this file, arches_karel should
solve the "repair the quad" problem (or Charles Bridge, or Efes).
"""
def turn_around():
    turn_left()
    turn_left()

def fix_column():
    """
    Karel fixes a single column
    """
    turn_left()
    for i in range(5):
        put_beeper()
        if front_is_clear():
            move() # fencepost issue
def move_four_times():
    for i in range(4):
        move()

def return_to_ground():
    turn_around()
    move_four_times()

def move_to_column():
    move_four_times()


def main():
    """
    You should write your code to make Karel do its task in
    this function. Make sure to delete the 'pass' line before
    starting to write your own code. You should also delete this
    comment and replace it with a better, more descriptive one.
    """
    for i in range(4):
        fix_column()
        return_to_ground()
        turn_left()
        if front_is_clear(): # fencepost issue
            move_to_column()



# There is no need to edit code beyond this point

if __name__ == "__main__":
    run_karel_program()