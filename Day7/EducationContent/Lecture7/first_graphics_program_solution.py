"""
File: first_graphics_program_solution.py
-------------------
Shows the awesomeness of graphics.
"""

from graphics import Canvas


def main():
    canvas = Canvas()
    rect = canvas.create_rectangle(50, 50, 200, 250)
    canvas.set_color(rect, 'red')
    canvas.mainloop()


if __name__ == '__main__':
    main()
