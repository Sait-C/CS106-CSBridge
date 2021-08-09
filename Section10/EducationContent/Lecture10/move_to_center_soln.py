"""
File: move_to_center.py
------------------------
This program draws a square on the screen and animates it towards the middle.
"""

from graphics import Canvas
import time

SQUARE_SIZE = 100
DELAY = 1 / 50


def main():
    # setup done once
    canvas = Canvas()
    canvas.set_canvas_title("Move to Center")
    square_top_y = canvas.get_canvas_height() / 2 - SQUARE_SIZE / 2
    rect = canvas.create_rectangle(0, square_top_y, SQUARE_SIZE, square_top_y + SQUARE_SIZE)
    canvas.set_color(rect, "black")

    # Animate the square until it reaches the center of the canvas
    while is_not_past_center(canvas, rect):
        # update world
        canvas.move(rect, 1, 0)
        canvas.update()

        # pause
        time.sleep(DELAY)

    canvas.mainloop()


def is_not_past_center(canvas, rect):
    """
    returns True if the rectangle is not past the center, or False otherwise.
    """
    x = canvas.get_left_x(rect)
    return x <= canvas.get_canvas_width() / 2 - canvas.get_width(rect) / 2


if __name__ == '__main__':
    main()
