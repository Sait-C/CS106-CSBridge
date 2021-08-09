"""
File: programming_is_awesome.py
--------------------
This program draws various art on the canvas using graphics!
"""
from graphics import Canvas

CANVAS_WIDTH = 1440
CANVAS_HEIGHT = 900


def draw_rectangle(canvas, x1, y1, x2, y2, color):
    rect = canvas.create_rectangle(x1, y1, x2, y2)
    canvas.set_fill_color(rect, color)
    return rect

def main():
    text = "Programming is Awesome!"
    canvas = Canvas(CANVAS_WIDTH, CANVAS_HEIGHT)
    canvas.set_canvas_title(text)


    draw_rectangle(canvas, 200, 200, 400, 1000, 'red')
    draw_rectangle(canvas, 1000, 700, 900, 100, 'yellow')
    draw_rectangle(canvas, 700, 400, 600, 300, 'blue')

    x = canvas.get_canvas_width() / 2
    y = canvas.get_canvas_height() / 2

    label = canvas.create_text(x, y, text)
    canvas.set_font(label, "Courier", 70)

    canvas.mainloop()


if __name__ == '__main__':
    main()
