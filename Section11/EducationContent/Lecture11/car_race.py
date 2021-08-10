"""
File: move_to_center.py
------------------------
This program implements a car race.
"""

from graphics import Canvas
import time
import random

CAR_WIDTH = 75
DELAY = 0.01
NUM_CARS = 10
MAX_SPEED = 4 # Speed in pixels


def main():
    # setup
    canvas = Canvas(800, 400)
    canvas.set_canvas_title("Formula 1")
    finish_x = 700
    finish_line = canvas.create_line(finish_x, 0, finish_x, canvas.get_canvas_height())
    canvas.set_color(finish_line, "red")

    colors = ['red','green','blue','yellow','black','white','cyan','purple']

    car_height = canvas.get_canvas_height() // (2 * NUM_CARS)

    # Create many cars and put them in a list
    cars = []
    for i in range(NUM_CARS):
        car_top_y = i * (car_height * 2)
        cars.append(canvas.create_rectangle(0, car_top_y, CAR_WIDTH, car_top_y + car_height))
        canvas.set_fill_color(cars[i], random.choice(colors))

    # Animate the square until it reaches the center of the canvas
    while is_not_past_finish(canvas, cars, finish_x):
        # update world: move each car in the cars list by a random amount
        for i in range(NUM_CARS):
            canvas.move(cars[i], random.randint(1, MAX_SPEED), 0)
        canvas.update()

        # pause
        time.sleep(DELAY)

    canvas.mainloop()


def is_not_past_finish(canvas, cars, finish_x):
    """
    returns True if the rectangle is not past the finish line, or False otherwise.
    """
    finish_reached = False
    for i in range(len(cars)):
        # get x of the right end of the car
        x = canvas.get_left_x(cars[i]) + canvas.get_width(cars[i])
        if x >= finish_x:
            finish_reached = True

    return not finish_reached


if __name__ == '__main__':
    main()
