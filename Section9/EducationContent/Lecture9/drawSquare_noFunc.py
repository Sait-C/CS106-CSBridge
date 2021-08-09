"""
File: checkerboard_drawSquare_noFunc.py
---------------------
This program draws a black square .
"""

from graphics import Canvas

SQUARE_SIZE = 60

def main():
    canvas = Canvas(120, 120)
    x = 30
    y = 30
    is_black = True
    square = canvas.create_rectangle(x, y, x + SQUARE_SIZE, y + SQUARE_SIZE)
    if is_black:
        color = 'black'
    else:
        color = 'white'
    canvas.set_fill_color(square, color)

    canvas.mainloop()





if __name__ == '__main__':
    main()
