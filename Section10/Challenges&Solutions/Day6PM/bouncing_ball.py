"""
File: bouncing_ball.py
---------------------
This program animates a ball (circle) bouncing around the screen.
"""

from graphics import Canvas

# Needed to place the ball randomly on the canvas.  Don't remove this.
import random

# Needed to delay the animation.  Don't remove this.
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
    dx = BALL_SPEED
    dy = BALL_SPEED

    while True:
        canvas.move(ball, dx, dy)
        canvas.update()
        time.sleep(DELAY)
        # Check for left/right collisions
        if canvas.get_left_x(ball) < 0 or canvas.get_left_x(ball) > canvas.get_canvas_width() - (BALL_RADIUS * 2):
            dx = -dx
        # Check for top/bottom collisions
        elif canvas.get_top_y(ball) < 0 or canvas.get_top_y(ball) > canvas.get_canvas_height() - (BALL_RADIUS * 2):
            dy = -dy
    canvas.mainloop()

def make_ball(canvas):
    """
    Creates a blue circle and places it at a random initial location on the screen.
    Returns the circle.
    """
    random_x = random.randint(0, canvas.get_canvas_width() - 2 * BALL_RADIUS)
    random_y = random.randint(0, canvas.get_canvas_height() - 2 * BALL_RADIUS)
    ball = canvas.create_oval(random_x, random_y, random_x + 2 * BALL_RADIUS, random_y + 2 * BALL_RADIUS)
    canvas.set_color(ball, 'blue')
    return ball

if __name__ == "__main__":
    main()