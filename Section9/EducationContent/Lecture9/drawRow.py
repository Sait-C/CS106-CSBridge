"""
File: checkerboard_drawRow.py
---------------------
This program draws a row of squares calling a draw_square function
within a for loop.
"""

from graphics import Canvas

SQUARE_SIZE = 60
NUM_ROWS = 8
NUM_COLS = 8

def main():
    canvas = Canvas(500, 200)
    is_black = True
    draw_row(canvas, NUM_COLS, 10, 10, is_black)
    is_black = False
    draw_row(canvas, NUM_COLS, 10, 100, is_black)
    canvas.mainloop()

def draw_row(canvas, num_squares, x0, y0, is_black):
    for i in range(num_squares):
        x = x0 + i * SQUARE_SIZE
        draw_square(canvas, x, y0, is_black)
        is_black = not is_black

def draw_square(canvas, x, y, is_black):
    square = canvas.create_rectangle(x , y, x + SQUARE_SIZE, y + SQUARE_SIZE)
    if is_black:
        color = 'black'
    else:
        color = 'white'
    canvas.set_color(square, color)
    canvas.set_outline_color(square, 'black')


if __name__ == '__main__':
    main()
