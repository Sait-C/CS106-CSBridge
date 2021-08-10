"""
File: catch_me_if_you_can.py
-------------------
This program draws several black "distractor" squares on the screen, along with a blue square that the user
tries to touch with their mouse.  But whenever the mouse touches the blue square, it moves to
another new random location!
"""

from graphics import Canvas
import random

# The dimensions of each black distractor square
DISTRACTOR_SIZE = 50

#The color of black squares on screen
DISTRACTOR_COLOR = "BLACK"

# The number of black squares on screen
N_DISTRACTORS = 20

# The dimensions of the blue square the user is trying to touch with the mouse
GOAL_SIZE = 60

#The color of the blue square the user is trying to touch with the mouse
GOAL_COLOR = "BLUE"

def main():
    # Create canvas with default size
    canvas = Canvas()
    canvas.set_canvas_title("Catch Me If You Can")

    # Create random black squares
    for i in range(N_DISTRACTORS):
        create_square_in_random_place(canvas, DISTRACTOR_SIZE, DISTRACTOR_COLOR)

    # Create our goal blue square in random location
    goal = create_square_in_random_place(canvas, GOAL_SIZE, GOAL_COLOR)
    while True:
        # Get mouse locations
        mouse_x = canvas.get_mouse_x()
        mouse_y = canvas.get_mouse_y()

        # Check for overlapping object with mouse, then check if it is goal and if it is, set random location for goal
        overlapping_objects = canvas.find_overlapping(mouse_x, mouse_y, mouse_x,mouse_y)
        canvas.update()
        for overlapping_object in overlapping_objects:
            if overlapping_object is goal:
                set_random_location(canvas, overlapping_object)


    canvas.mainloop()

def set_random_location(canvas, shape):
    # Get canvas width, height and shape's width for calculate the random x and y value's end points
    canvas_width = canvas.get_canvas_width()
    canvas_height = canvas.get_canvas_height()
    widht_of_shape = canvas.get_width(shape)

    # Calculate the random x and y locations
    randX = random.randint(0, canvas_width - widht_of_shape)
    randY = random.randint(0, canvas_height - widht_of_shape)

    # Move shape to this random location
    canvas.moveto(shape, randX, randY)
    # Update canvas for changes
    canvas.update()

def create_square_in_random_place(canvas, size_of_square, color):
    x = random.randint(0, canvas.get_canvas_width() - size_of_square)
    y = random.randint(0, canvas.get_canvas_height() - size_of_square)
    rect = canvas.create_rectangle(x, y, x + size_of_square, y + size_of_square)
    canvas.set_fill_color(rect, color)
    canvas.update()
    return rect


if __name__ == '__main__':
    main()
