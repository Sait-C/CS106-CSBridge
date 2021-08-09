"""
File: checkerboard_alternative.py
---------------------
This program draws a checkerboard. Alternative implementation
"""

from graphics import Canvas

SQUARE_SIZE = 30
NUM_ROWS = 8
NUM_COLS = 8

def main():
    canvas = Canvas(260, 260)
    is_black = True
    x0 = 10
    y0 = 10
    for i in range(NUM_ROWS):
        for j in range(NUM_COLS):
            x = x0 + j * SQUARE_SIZE
            y = y0 + i * SQUARE_SIZE
            is_black = (i + j) % 2 == 0
            draw_square(canvas, x, y, is_black)

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
