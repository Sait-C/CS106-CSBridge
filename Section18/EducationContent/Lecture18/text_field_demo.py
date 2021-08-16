"""
File: text_field_demo.py
-------------------
A program that adds a text_field, text and button on canvas and
read from input and updated text when clicked on button
"""

from graphics import Canvas


def main():
    canvas = Canvas()
    canvas.set_canvas_title("Read Text")

    # Create the interactors (text field and 1 button)

    canvas.create_text_field("Input", Canvas.BOTTOM)

    text1 = canvas.create_text(40, 40, 'I am a text')
    canvas.create_button("Read Text", Canvas.BOTTOM)

    while True:
        button_clicks = canvas.get_new_button_clicks()
        for button_click in button_clicks:

            if button_click == "Read Text":
                # Get the contents of the input text field
                user_text = canvas.get_text_field_text("Input")
                print(user_text)
                canvas.set_text(text1, user_text)

        canvas.update()

    canvas.mainloop()


if __name__ == '__main__':
    main()
