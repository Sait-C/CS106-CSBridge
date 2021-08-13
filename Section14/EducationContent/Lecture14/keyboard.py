"""
File: keyboard.py
-------------------
This is a program that lets us try out keyboard events.
"""

from graphics import Canvas


def main():
    canvas = Canvas()
    canvas.set_canvas_title("Keyboard")

    # Create a centered label to display the symbol for the key that was pressed
    label = canvas.create_text(canvas.get_canvas_width() / 2,
                               canvas.get_canvas_height() / 2,
                               "Press a key!")
    canvas.set_font(label, "Courier", 30)

    while True:
        # For each key, display its symbol on the screen
        presses = canvas.get_new_key_presses()
        for press in presses:
            canvas.set_text(label, press.keysym)

        canvas.update()

    canvas.mainloop()


if __name__ == "__main__":
    main()
