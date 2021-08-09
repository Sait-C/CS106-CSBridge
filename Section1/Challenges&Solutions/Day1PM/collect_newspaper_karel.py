from karel.stanfordkarel import *

def turn_right():
    for i in range(3):
        turn_left()
def turn_around():
    turn_left()
    turn_left()

def move_to_newspaper():
    turn_right()
    move()
    turn_left()
    for i in range(3):
        move()

def move_to_start():
    for i in range(3):
        move()
    turn_right()
    move()

def main():
    move_to_newspaper()
    pick_beeper()
    move_to_start()

if __name__ == "__main__":
    run_karel_program()