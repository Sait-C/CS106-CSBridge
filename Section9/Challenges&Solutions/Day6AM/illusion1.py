"""
File: illusion1.py
------------------------
This program draws an optical illusion of a checkerboard pattern.
"""

from graphics import Canvas


# These constants tell the graphics canvas how big to be.  You can ignore them.
# Use get_canvas_width() and get_canvas_height() instead.
CANVAS_WIDTH = 540
CANVAS_HEIGHT = 430

# The size of each dimension of the square. use this!
SIZE = 100

# The space between two squares. Use this!
GAP = 10


def main():
    canvas = Canvas(CANVAS_WIDTH, CANVAS_HEIGHT)
    canvas.set_canvas_title("Illusion 1")

    for i in range(5):
        for j in range(4):
            x = i * (SIZE + GAP)
            y = j * (SIZE + GAP)
            square = canvas.create_rectangle(x, y, x + SIZE, y + SIZE)
            canvas.set_fill_color(square, "BLACK")
    canvas.mainloop()


if __name__ == '__main__':
    main()
