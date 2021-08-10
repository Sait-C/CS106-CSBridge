"""
File: car_race_starter.py
------------------------
Starter code for a program that implements a car race.
"""

from graphics import Canvas
import time
import random

CAR_WIDTH = 75
CAR_HEIGHT = 25
DELAY = 0.002
NUM_CARS = 10


def main():
    # setup
    canvas = Canvas(500, 400)
    canvas.set_canvas_title("Formula 1")
    finish_x = 400
    finish_line = canvas.create_line(finish_x, 0, finish_x, canvas.get_canvas_height())
    canvas.set_color(finish_line, "red")

    colors = ['red','green','blue','yellow','black','white','cyan','purple']

    car_top_y = 0
    rect = canvas.create_rectangle(0, car_top_y, CAR_WIDTH, car_top_y + CAR_HEIGHT)
    canvas.set_color(rect, random.choice(colors))

    # Animate the square until it reaches the center of the canvas
    while is_not_past_finish(canvas, rect, finish_x):
        # update world
        canvas.move(rect, 2, 0)
        canvas.update()

        # pause
        time.sleep(DELAY)

    canvas.mainloop()


def is_not_past_finish(canvas, rect, finish_x):
    """
    returns True if the rectangle is not past the finish line, or False otherwise.
    """
    # get x of the right end of the car
    x = canvas.get_left_x(rect) + canvas.get_width(rect)
    return x <= finish_x


if __name__ == '__main__':
    main()
