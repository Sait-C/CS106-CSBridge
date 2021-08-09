"""
File: checkerboard_drawSquare.py
---------------------
This program draws a square defining and calling a draw_square() function.
"""

from graphics import Canvas

SQUARE_SIZE = 60


def main():
    canvas = Canvas(120, 120)
    draw_square(canvas, 30, 30, True)
    canvas.mainloop()


def draw_square(canvas, x, y, is_black):
    square = canvas.create_rectangle(x, y, x + SQUARE_SIZE, y + SQUARE_SIZE)
    if is_black:
        color = 'black'
    else:
        color = 'white'
    canvas.set_fill_color(square, color)


if __name__ == '__main__':
    main()
