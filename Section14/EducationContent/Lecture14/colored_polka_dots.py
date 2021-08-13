"""
File: colored_polka_dots.py
-------------------
This is a program that adds a circle to the canvas wherever the user
clicks the mouse.  All the polka dots change to a new random color
whenever the user hits the space bar.
"""

from graphics import Canvas

CIRCLE_SIZE = 25


def main():
    canvas = Canvas()
    canvas.set_canvas_title("Colored Polka Dots")

    while True:
        # Add a circle each time the user clicks
        clicks = canvas.get_new_mouse_clicks()
        for click in clicks:
            create_polka_dot(canvas, click.x, click.y)

        canvas.update()

    canvas.mainloop()


def create_polka_dot(canvas, x, y):
    """
    Creates a new polka dot on the canvas with upper-left corner
    at the given x, y location, colored blue.
    """
    circle = canvas.create_oval(x, y, x + CIRCLE_SIZE, y + CIRCLE_SIZE)
    canvas.set_color(circle, 'blue')


if __name__ == "__main__":
    main()
