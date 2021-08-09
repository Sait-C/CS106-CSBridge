"""
File: centering_solution.py
-------------------
Shows how to center a graphical object on the canvas.
"""

from graphics import Canvas

RECTANGLE_WIDTH = 150
RECTANGLE_HEIGHT = 200


def main():
    canvas = Canvas()
    rect_x = canvas.get_canvas_width() / 2 - RECTANGLE_WIDTH / 2
    rect_y = canvas.get_canvas_height() / 2 - RECTANGLE_HEIGHT / 2
    rect = canvas.create_rectangle(rect_x, rect_y, rect_x + RECTANGLE_WIDTH, rect_y + RECTANGLE_HEIGHT)
    canvas.set_color(rect, 'red')
    canvas.mainloop()


if __name__ == '__main__':
    main()
