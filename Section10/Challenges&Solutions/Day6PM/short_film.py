"""
File: short_film.py
----------------
Creates a short animated film with a sunset to start off with.
"""

from graphics import Canvas
import time
import math

SUN_RADIUS = 25

# The amount the sun should move down the screen each frame
DESCENT = 2

# in seconds
DELAY = 0.03

INTRO_MESSAGE = "Once Upon a Time..."
INTRO_MESSAGE_FONT = "Papyrus"
INTRO_MESSAGE_SIZE = 40
INTRO_MESSAGE_COLOR = "WHITE"

OUTRO_MESSAGE = "The End"
OUTRO_MESSAGE_FONT = "Papyrus"
OUTRO_MESSAGE_SIZE = 40
OUTRO_MESSAGE_COLOR = "WHITE"

FLOOR_COLOR = "GREEN"

SKY_COLOR = "BLUE"
SUN_COLOR_LOW = "YELLOW"
SUN_COLOR_MEDIUM = "ORANGE"
SUN_COLOR_HIGH = "RED"
INTRO_BACKGROUND_COLOR = "BLACK"

FLOOR_HEIGHT_DIVIDER  = 1.6
get_floor_height = lambda canvas_height: canvas_height / FLOOR_HEIGHT_DIVIDER


def main():
    canvas = Canvas()
    canvas.set_canvas_title("Short Film")

    display_message(canvas, 2, INTRO_MESSAGE, INTRO_MESSAGE_FONT, INTRO_MESSAGE_COLOR, INTRO_MESSAGE_SIZE)
    sun, floor = draw_scene(canvas)
    animate_sun(canvas, sun)
    delete_objects(canvas, sun, floor)
    display_message(canvas, 3, OUTRO_MESSAGE, OUTRO_MESSAGE_FONT, OUTRO_MESSAGE_COLOR, OUTRO_MESSAGE_SIZE)
    canvas.destroy()

def delete_objects(canvas, *args):
    for obj in args:
        canvas.delete(obj)

def display_message(canvas, delay, message, font, color, size):
    canvas.set_canvas_background_color(INTRO_BACKGROUND_COLOR)
    canvas_width = canvas.get_canvas_width()
    canvas_height = canvas.get_canvas_height()
    label = canvas.create_text(canvas_width/2, canvas_height/2, message)
    canvas.set_font(label, font, size)
    canvas.set_fill_color(label, color)
    canvas.update()
    time.sleep(delay)
    canvas.delete(label)

def draw_scene(canvas):
    canvas.set_canvas_background_color(SKY_COLOR)
    sun = draw_sun(canvas)
    floor = draw_floor(canvas)
    return sun, floor

def draw_sun(canvas):
    canvas_width = canvas.get_canvas_width()
    canvas_height = canvas.get_canvas_height()

    x = (canvas_width / 2) - SUN_RADIUS
    y = (canvas_height / 2) - (canvas_height / 2.2)
    sun = canvas.create_oval(x, y, x + (SUN_RADIUS * 2), y + (SUN_RADIUS * 2))
    canvas.set_fill_color(sun, SUN_COLOR_LOW)
    return sun

def draw_floor(canvas):
    canvas_width = canvas.get_canvas_width()
    canvas_height = canvas.get_canvas_height()

    y = get_floor_height(canvas_height)
    floor = canvas.create_rectangle(0, y, canvas_width, y + canvas_height)
    canvas.set_fill_color(floor, FLOOR_COLOR)
    return floor

def animate_sun(canvas, sun):
    canvas_height = canvas.get_canvas_height()
    center = 0
    while True:
        canvas.move(sun, 0, DESCENT)
        canvas.update()
        top_y = canvas.get_top_y(sun)
        center_y = top_y + SUN_RADIUS
        sun_color = get_sun_color(center_y, get_floor_height(canvas_height))
        canvas.set_fill_color(sun, sun_color)
        if check_is_sun_in_floor_height(center_y, get_floor_height(canvas_height)):
            print(center_y)
            print(get_floor_height(canvas_height))
            break
        time.sleep(DELAY)

def get_sun_color(y, floor_height):
    if y < floor_height / 3:
        return SUN_COLOR_LOW
    elif y > floor_height / 3 and y < floor_height / 1.2:
        return SUN_COLOR_MEDIUM
    else:
        return SUN_COLOR_HIGH


def check_is_sun_in_floor_height(y, floor_height):
    return y >= floor_height

if __name__ == '__main__':
    main()
