"""
File: bouncing_ball.py
---------------------
This program animates a ball (circle) bouncing around the screen.
"""

from graphics import Canvas
import random
import time

# Size of the ball
BALL_RADIUS = 20

# Seconds to pause each animation cycle
DELAY = 0.02

"""
The value of the speed in the x and y direction the ball should travel.
In other words, the ball will be traveling either +5 or -5 in the x direction, and
+5 or -5 in the y direction, at all times.
"""
BALL_SPEED = 5


def main():
    canvas = Canvas()
    canvas.set_canvas_title("Bouncing Ball")

    ball = make_ball(canvas)
    change_x = BALL_SPEED
    change_y = BALL_SPEED

    while True:
        canvas.move(ball, change_x, change_y)
        canvas.update()
        time.sleep(DELAY)

    canvas.mainloop()


def make_ball(canvas):
    """
    Creates a blue circle and places it at (0,0) on the screen.
    Returns the circle.
    """
    ball = canvas.create_oval(0, 0, 2 * BALL_RADIUS, 2 * BALL_RADIUS)
    canvas.set_color(ball, 'blue')
    return ball


if __name__ == "__main__":
    main()
