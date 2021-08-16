"""
File: button_demo.py
-------------------
A program that adds buttons on canvas and respond to button clicks
"""

from graphics import Canvas
import random


def main():
    canvas = Canvas()
    canvas.set_canvas_title("Button Demo")

    # Create the interactors (create 2 buttons)

    canvas.create_button("Click Me", Canvas.TOP)
    canvas.create_button("Don't Click me", Canvas.BOTTOM)

    while True:
        button_clicks = canvas.get_new_button_clicks()
        for button_click in button_clicks:
            if button_click == "Click Me":
                print('Thanks for clicking')
            elif button_click == "Don't Click me":
                print('Hey why did u click')
        canvas.update()

    canvas.mainloop()


if __name__ == '__main__':
    main()
