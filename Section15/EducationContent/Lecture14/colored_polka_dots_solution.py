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

    dots = []

    while True:
        # Add a circle each time the user clicks
        clicks = canvas.get_new_mouse_clicks()
        for click in clicks:
            dot = create_polka_dot(canvas, click.x, click.y)
            dots.append(dot)

        # If the user hits the space bar, change the dots to random colors
        presses = canvas.get_new_key_presses()
        for press in presses:
            if press.keysym == "space":
                randomly_color_dots(canvas, dots)

        canvas.update()

    canvas.mainloop()


def create_polka_dot(canvas, x, y):
    """
    Creates and returns a new polka dot on the canvas with upper-left corner
    at the given x, y location, colored blue.
    """
    circle = canvas.create_oval(x, y, x + CIRCLE_SIZE, y + CIRCLE_SIZE)
    canvas.set_color(circle, 'blue')
    return circle


def randomly_color_dots(canvas, dots):
    """
    Randomly colors all the dots in the dots list to be
    different random colors.
    """
    for dot in dots:
        random_color = canvas.get_random_color()
        canvas.set_color(dot, random_color)


if __name__ == "__main__":
    main()
