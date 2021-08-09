"""
File: mystery_square.py
-------------------
This program creates a centered square that changes color randomly every second.
"""

from graphics import Canvas

# Needed for pausing for animation.  Don't remove this.
import time

# Size of the centered square
SQUARE_SIZE = 400

# Delay between color changes, in seconds
DELAY = 1


def main():
    canvas = Canvas()
    canvas.set_canvas_title("Mystery Square")

    square = draw_square_to_center(canvas, SQUARE_SIZE)
    while True:
        randomColor = canvas.get_random_color()
        canvas.set_fill_color(square, randomColor)
        canvas.update()
        time.sleep(DELAY)

    canvas.mainloop()


def draw_square_to_center(canvas, square_width):
    canvas_width = canvas.get_canvas_width()
    canvas_height = canvas.get_canvas_height()
    x = (canvas_width / 2) - (square_width / 2)
    y = (canvas_height / 2) - (square_width / 2)
    square = canvas.create_rectangle(x, y, x + square_width, y + square_width)

    return square

if __name__ == "__main__":
    main()
