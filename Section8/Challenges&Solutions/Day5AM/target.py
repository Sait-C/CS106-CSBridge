"""
File: target.py
---------------
This program draws a red and white target symbol in the center of the screen.
"""

from graphics import Canvas

# The sizes of the concentric circles
BIG_CIRCLE_RADIUS = 150
MEDIUM_CIRCLE_RADIUS = 100
SMALL_CIRCLE_RADIUS = 50


def main():
    canvas = Canvas()
    canvas.set_canvas_title("Target")

    big_oval = create_centered_oval(canvas, BIG_CIRCLE_RADIUS)
    canvas.set_fill_color(big_oval, "RED")
    medium_oval = create_centered_oval(canvas, MEDIUM_CIRCLE_RADIUS)
    canvas.set_fill_color(medium_oval, "WHITE")
    small_oval = create_centered_oval(canvas, SMALL_CIRCLE_RADIUS)
    canvas.set_fill_color(small_oval, "RED")

    canvas.mainloop()


def create_centered_oval(canvas, radius):
    canvas_height = canvas.get_canvas_height()
    canvas_weidth = canvas.get_canvas_width()
    oval = canvas.create_oval((canvas_weidth / 2) - radius, (canvas_height / 2) - radius,
                       (canvas_weidth / 2) + radius, (canvas_height / 2) + radius)
    return oval
if __name__ == '__main__':
    main()
