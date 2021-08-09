"""
File: draw_car_solution.py
-----------------------
Draws a car in the top left corner of the screen
"""
from graphics import Canvas


def main():
    canvas = Canvas()
    canvas.set_canvas_title("Car")
    canvas.set_canvas_background_color("yellow")

    # Car body
    body = canvas.create_rectangle(10, 30, 110, 80)
    canvas.set_fill_color(body, "blue")

    # Car wheels
    wheel1 = canvas.create_oval(20, 70, 40, 90)
    canvas.set_fill_color(wheel1, "red")
    wheel2 = canvas.create_oval(80, 70, 100, 90)
    canvas.set_fill_color(wheel2, "red")

    # Windshield
    windshield = canvas.create_rectangle(80, 40, 110, 60)
    canvas.set_fill_color(windshield, "cyan")

    canvas.mainloop()


if __name__ == "__main__":
    main()
