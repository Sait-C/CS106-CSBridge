"""
File: loop_art_solution.py
-------------------
Shows how to combine loops and graphics to create cool patterns.
"""

from graphics import Canvas


def main():
    canvas = Canvas()
    for i in range(10):
        circle_x = 100 + 20 * i
        circle_y = 5 + 20 * i
        canvas.create_oval(circle_x, circle_y, circle_x + 50, circle_y + 50)
    canvas.mainloop()


if __name__ == '__main__':
    main()
