"""
File: mouse_location.py
-------------------
This program displays a label in the center of the screen displaying the current mouse coordinates.
"""

from graphics import Canvas


def main():
    canvas = Canvas()
    canvas.set_canvas_title("Mouse Location")
    canvas.set_canvas_background_color("BLACK")

    canvas_width = canvas.get_canvas_width()
    canvas_height = canvas.get_canvas_height()
    text = canvas.create_text(canvas_width / 2, canvas_height / 2, "(x, y)")
    canvas.set_font(text, "Small Font", 50)
    canvas.set_fill_color(text, "WHITE")

    while True:
        x = canvas.get_mouse_x()
        y = canvas.get_mouse_y()

        textContent = f"({x},{y})"
        canvas.set_text(text, textContent)

        canvas.update()


    canvas.mainloop()


if __name__ == "__main__":
    main()
