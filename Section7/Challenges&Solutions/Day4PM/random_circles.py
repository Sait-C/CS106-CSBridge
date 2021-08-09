"""
File: random_circles.py
-------------------
Draws 10 random circles such that each circle is on the screen.
"""

from graphics import Canvas
# this is needed to generate random numbers.  Don't delete this.
import random

# The number of circles to draw
NUM_CIRCLES = 10


CANVAS_WIDTH = 720
CANVAS_HEIGHT = 480

MIN_RADIUS = 50
MAX_RADIUS = 200

def main():
    canvas = Canvas(CANVAS_WIDTH, CANVAS_HEIGHT)
    canvas.set_canvas_title("Random Circles")

    for i in range(NUM_CIRCLES):
        while True:
            x1 = random.randint(0, CANVAS_WIDTH)
            y1 = random.randint(0, CANVAS_HEIGHT)
            radius = random.randint(MIN_RADIUS, MAX_RADIUS)
            x2 = x1 + radius
            y2 = y1 + radius
            if checkIfPastCanvasEdge(x2, y2):
                break
        circle = canvas.create_oval(x1, y1, x2, y2)
        canvas.set_fill_color(circle, canvas.get_random_color())

    canvas.mainloop()


def checkIfPastCanvasEdge(x, y):
    return (x <= CANVAS_WIDTH and y <= CANVAS_HEIGHT)


# call the function
if __name__ == '__main__':
    main()
