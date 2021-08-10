"""
File: making_tracks.py
-------------------
This program draws a track wherever the user clicks the mouse.
"""

from graphics import Canvas


def main():
    canvas = Canvas()
    canvas.set_canvas_title("Making Tracks")

    while True:
        # Get user input
        clicks = canvas.get_new_mouse_clicks()
        for click in clicks:
            # Add an image for each click
            canvas.create_image_with_size(click.x, click.y, 20, 20, "images/simba.jpg")

        canvas.update()
    canvas.mainloop()

    canvas.mainloop()


if __name__ == '__main__':
    main()