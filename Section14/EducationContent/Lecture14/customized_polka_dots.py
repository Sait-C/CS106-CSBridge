"""
File: customized_polka_dots.py
-------------------
This is a program that adds a circle to the canvas wherever the user
clicks the mouse.  The color that the polka dot is drawn with can be
changed by hitting different keys on the keyboard (e.g. r = red, b = blue,
o = orange).
"""

from graphics import Canvas

CIRCLE_SIZE = 25


def main():
    canvas = Canvas()
    canvas.set_canvas_title("Colored Polka Dots")

    # Track the color that we should use to draw the next dot
    current_color = 'blue'

    while True:
        # Add a circle each time the user clicks
        clicks = canvas.get_new_mouse_clicks()
        for click in clicks:
            create_polka_dot(canvas, click.x, click.y, current_color)

        # If the user hits the space bar, change the dots to random colors
        presses = canvas.get_new_key_presses()
        for press in presses:
            if press.keysym == 'r':
                current_color = 'red'
            elif press.keysym == 'o':
                current_color = 'orange'
            elif press.keysym == 'b':
                current_color = 'blue'

        canvas.update()

    canvas.mainloop()


def create_polka_dot(canvas, x, y, color):
    """
    Creates and returns a new polka dot on the canvas with upper-left corner
    at the given x, y location, colored the given color.
    """
    circle = canvas.create_oval(x, y, x + CIRCLE_SIZE, y + CIRCLE_SIZE)
    canvas.set_color(circle, color)


if __name__ == "__main__":
    main()
