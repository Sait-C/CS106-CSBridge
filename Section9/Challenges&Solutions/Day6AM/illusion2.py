"""
File: illusion2.py
------------------------
This program draws an optical illusion of an off-checkerboard pattern.
"""

from graphics import Canvas
import math

# These constants tell the graphics canvas how big to be.  You can ignore them.
# Use get_canvas_width() and get_canvas_height() instead.
CANVAS_WIDTH = 800
CANVAS_HEIGHT = 500

# The height of each row, and the size of each square. use this!
SQUARE_SIZE = 50

# The number of rows.  Use this!
NUM_ROWS = 10


def main():
    canvas = Canvas(CANVAS_WIDTH, CANVAS_HEIGHT)
    canvas.set_canvas_title("Illusion 2")
    x0 = 15
    y0 = 0
    offset = 0
    for i in range(NUM_ROWS):
        y = y0 + i * SQUARE_SIZE
        offset = math.sin(i / 1.5) * SQUARE_SIZE/4
        draw_row(canvas, x0, y, 8, SQUARE_SIZE, offset)

    canvas.mainloop()


def draw_row(canvas, x0, y0, n, square_size, offset):
    line = canvas.create_line(x0, y0, CANVAS_WIDTH, y0)
    canvas.set_fill_color(line, "GREY")
    for i in range(n):
        x = x0 + i * (square_size * 2)
        draw_square(canvas, x+offset, y0, square_size, offset)

def draw_square(canvas, x, y, square_size, offset, outline_color = "GREY", fill_color = "BLACK"):
    square = canvas.create_rectangle(x, y, x + square_size, y + square_size)
    canvas.set_outline_color(square, outline_color)
    canvas.set_fill_color(square, fill_color)

if __name__ == '__main__':
    main()
