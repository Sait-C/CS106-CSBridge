"""
File: snow.py
-------------
Animates snow falling from the top to the bottom of the screen.  Snowflakes will be randomly added at the top at
random locations, and animated downwards together until they reach the bottom of the screen.
"""

from graphics import Canvas
import random
import time

ANIMATION_DELAY_SECONDS = 0.001
SNOWFLAKE_DIAMETER = 10


def main():
    canvas = Canvas()
    canvas.set_canvas_title("Snow")

    snowflakes = [] # Keeps track of all of our snowflakes
    while True:
        # Get the snowflakes to update
        # 1) Generate new snowflake with 10% probability
        create_new_snowflake(canvas, snowflakes)
        # 2) Snowflakes to move down if they're not at the bottom
        for snowflake in snowflakes:
            if canvas.get_top_y(snowflake) <= canvas.get_canvas_height() - SNOWFLAKE_DIAMETER:
                canvas.move(snowflake, 0, 1)

        canvas.update()
        time.sleep(ANIMATION_DELAY_SECONDS)

    canvas.mainloop()

def create_new_snowflake(canvas, snowflakes):
    if random.random() <= 0.1: # -> 0 - 1
        x = random.randint(0, canvas.get_canvas_width() - SNOWFLAKE_DIAMETER) # Any random x coordinate on the canvas
        snowflake = canvas.create_oval(x, 0, x + SNOWFLAKE_DIAMETER, SNOWFLAKE_DIAMETER)
        canvas.set_fill_color(snowflake, 'black')
        snowflakes.append(snowflake)

if __name__ == '__main__':
    main()