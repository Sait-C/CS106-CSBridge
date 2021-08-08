from karel.stanfordkarel import *


def main():
    for i in range(8):
        if front_is_clear():
            move()
        else:
            turn_left()
            while right_is_blocked():
                move()
            for i in range(3):
                turn_left()
            move()
            for i in range(3):
                turn_left()
            while front_is_clear():
                move()
            turn_left()


# There is no need to edit code beyond this point

if __name__ == "__main__":
    run_karel_program()
