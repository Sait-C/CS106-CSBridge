"""
File: breakout.py
-----------------
This program implements the game Breakout!  The user controls a paddle
moving horizontally with the mouse, and the user must bounce the ball
to make it collide and remove bricks from the screen.  The user has
3 turns.  If the ball falls below the bottom of the screen, the user
loses a turn.  If the user removes all bricks before their turns
run out, they win!
"""

import math
from graphics import Canvas
import random
import time

"""
Dimensions of the canvas, in pixels
These should be used when setting up the initial size of the game,
but in later calculations you should use canvas.get_canvas_width() and 
canvas.get_canvas_height() rather than these constants for accurate size information.
"""
CANVAS_WIDTH = 420
CANVAS_HEIGHT = 600

# Stage 1: Set up the Bricks

# Number of bricks in each row
NBRICK_COLUMNS = 10

# Number of rows of bricks
NBRICK_ROWS = 10

# Separation between neighboring bricks, in pixels
BRICK_SEP = 4

# Width of each brick, in pixels
BRICK_WIDTH = math.floor((CANVAS_WIDTH - (NBRICK_COLUMNS + 1.0) * BRICK_SEP) / NBRICK_COLUMNS)

# Height of each brick, in pixels
BRICK_HEIGHT = 8

# Offset of the top brick row from the top, in pixels
BRICK_Y_OFFSET = 70

# Stage 2: Create the Bouncing Ball

# Radius of the ball in pixels
BALL_RADIUS = 10

# The ball's vertical velocity.
VELOCITY_Y = 6.0

# The ball's minimum and maximum horizontal velocity; the bounds of the
# initial random velocity that you should choose (randomly +/-).
VELOCITY_X_MIN = 2.0
VELOCITY_X_MAX = 6.0

# Animation delay or pause time between ball moves (in seconds)
DELAY = 1 / 60

# Stage 3: Create the Paddle

# Dimensions of the paddle
PADDLE_WIDTH = 60
PADDLE_HEIGHT = 10

# Offset of the paddle up from the bottom
PADDLE_Y_OFFSET = 30

# Stage 5: Polish and Finishing Up

# Number of turns
NTURNS = 3

BOUNCE_SOUND = "bounce.au"

get_center_x_of_shape = lambda canvas, shape:  canvas.get_left_x(shape) + (canvas.get_width(shape) / 2)

number_of_turn = NTURNS
start = False
game_over = False
score = 0
def main():
    global number_of_turn
    global start
    global score

    score = 0
    number_of_turn = NTURNS
    canvas = Canvas(CANVAS_WIDTH, CANVAS_HEIGHT)
    canvas.set_canvas_title("Breakout")

    brick_list = []
    create_bricks(canvas, NBRICK_COLUMNS, 2, "RED", 5, BRICK_Y_OFFSET, BRICK_SEP, brick_list)
    create_bricks(canvas, NBRICK_COLUMNS, 2, "ORANGE", 5,BRICK_Y_OFFSET + (2 * BRICK_HEIGHT) + (BRICK_SEP*2), BRICK_SEP, brick_list)
    create_bricks(canvas, NBRICK_COLUMNS, 2, "YELLOW", 5, BRICK_Y_OFFSET + (4 * BRICK_HEIGHT) + (BRICK_SEP*4), BRICK_SEP, brick_list)
    create_bricks(canvas, NBRICK_COLUMNS, 2, "GREEN",5, BRICK_Y_OFFSET + (6 * BRICK_HEIGHT) + (BRICK_SEP*6), BRICK_SEP, brick_list)
    create_bricks(canvas, NBRICK_COLUMNS, 2, "BLUE", 5, BRICK_Y_OFFSET + (8 * BRICK_HEIGHT) + (BRICK_SEP*8), BRICK_SEP, brick_list)

    ball = create_ball(canvas)
    paddle = create_paddle(canvas)

    velocity_x = random.randint(VELOCITY_X_MIN, VELOCITY_X_MAX)
    velocity_x = velocity_x if random.choice([True, False]) == True else -velocity_x
    velocity_y = VELOCITY_Y

    while True:
        if check_mouse_is_in_game_area(canvas):
            movePaddle(canvas, paddle)

        clicks = canvas.get_new_mouse_clicks()
        if len(clicks) > 0 and not game_over:
            start = True

        if start and not game_over:
            moveBall(canvas, ball, velocity_x, velocity_y)
            direction_x, direction_y = check_bouncy(canvas, ball)
            velocity_x, velocity_y = change_direction(velocity_x, velocity_y, direction_x, direction_y)

            colliding_list = check_collision(canvas, ball)

            for col in colliding_list:
                if col is paddle:
                    change_x, change_y = handle_collision_with_paddle(canvas, paddle, ball, velocity_x)
                    velocity_x, velocity_y = change_direction(velocity_x, velocity_y, change_x, change_y)
                elif col is not ball:
                    change_x, change_y= handle_collision_with_brick(canvas, col, brick_list)
                    velocity_x, velocity_y = change_direction(velocity_x, velocity_y, change_x, change_y)
            check_if_finish_brick(canvas, brick_list)
    canvas.mainloop()

# -------------------------------GAME MANAGER---------------------------------
def check_if_finish_brick(canvas, brick_list):
    if len(brick_list) <= 0:
        game_won(canvas)

def game_won(canvas):
    start = False
    game_over = True
    write_letters(canvas, 30, "YOU WON !")

def damage(canvas, ball):
    global number_of_turn
    global start
    start = False
    number_of_turn -= 1

    if number_of_turn <= 0:
        gameOver(canvas, ball)
        return

    x = canvas.get_canvas_width() / 2 - BALL_RADIUS
    y = canvas.get_canvas_height() / 2 - BALL_RADIUS
    canvas.move_to(ball, x, y)
    canvas.update()

def gameOver(canvas, ball):
    global game_over
    game_over = True
    write_letters(canvas, 30, "GAME OVER...")
    #canvas.delete(ball)

def write_letters(canvas, size, text):
    textObj = canvas.create_text(canvas.get_canvas_width()/2, canvas.get_canvas_height()/2, "")
    canvas.set_font(textObj, "Papyrus", size)
    temp = ""
    for i in range(len(text)):
        temp += text[i]
        canvas.set_text(textObj, temp)
        canvas.update()
        time.sleep(0.2)

# -------------------------------BRICK---------------------------------
def create_bricks(canvas, columns, rows, color, x0, y0, sep, brick_list):
    for i in range(rows):
        y = (y0 + i * (BRICK_HEIGHT + sep))
        for j in range(columns):
            x = x0 + j * (BRICK_WIDTH + sep)
            rect = canvas.create_rectangle(x, y, x + BRICK_WIDTH, y + BRICK_HEIGHT)
            canvas.set_fill_color(rect, color)
            canvas.update()
            brick_list.append(rect)

# -------------------------------BALL---------------------------------
def handle_collision_with_paddle(canvas, paddle, ball, velocity_x):
    current_direction = velocity_x/abs(velocity_x)
    paddle_center_x = get_center_x_of_shape(canvas, paddle)
    ball_center_x = get_center_x_of_shape(canvas, ball)

    if (ball_center_x - paddle_center_x): # check if it is zero to not get a zero division error
        # if ball collide with paddle on the paddle's right, direction_x will be positive, if not, direction_x will be negative
        # direction_x == negative -> left collide
        # direction_x == positive -> right collide
        direction_x = (ball_center_x - paddle_center_x)/abs(ball_center_x - paddle_center_x)
    else:
        direction_x = 1

    if current_direction == 1 and direction_x == -1: # if ball goes to right and collide with the paddle's left
        return direction_x, -1 # go reverse direction
    elif current_direction == 1 and direction_x == 1: # if ball goes to right and collide with the paddle's right
        return direction_x, -1 # go same direction
    elif current_direction == -1 and direction_x == -1: # if ball goes to left and collide with the paddle's left
        return -direction_x, -1 # go reverse direction
    elif current_direction == -1 and direction_x == 1: # if ball goes to left and collide with the paddle's right
        return -direction_x, -1 # go reverse direction

def handle_collision_with_brick(canvas, col, brick_list):
    brick_list.remove(col)
    canvas.delete(col)
    return 1, -1

def change_direction(velocity_x, velocity_y, direction_x, direction_y):
    velocity_x = velocity_x * direction_x
    velocity_y = velocity_y * direction_y
    return velocity_x, velocity_y

def create_ball(canvas):
    x = canvas.get_canvas_width()/2 - BALL_RADIUS
    y = canvas.get_canvas_height()/2 - BALL_RADIUS
    ball = canvas.create_oval(x, y, x + BALL_RADIUS*2, y + BALL_RADIUS*2)
    canvas.set_fill_color(ball, "BLACK")
    return ball

def moveBall(canvas, ball, velocity_x, velocity_y):
    canvas.move(ball, velocity_x, velocity_y)
    time.sleep(DELAY)
    canvas.update()

def get_left_x_of_ball(canvas, ball):
    return canvas.get_left_x(ball)

def get_right_x_of_ball(canvas, ball):
    return get_left_x_of_ball(canvas, ball) + canvas.get_width(ball)

def get_top_y_of_ball(canvas, ball):
    return canvas.get_top_y(ball)

def get_bottom_y_of_ball(canvas, ball):
    return get_top_y_of_ball(canvas, ball) + canvas.get_width(ball)

def check_bouncy(canvas, ball):
    canvas_width = canvas.get_canvas_width()
    canvas_height = canvas.get_canvas_height()

    if (get_left_x_of_ball(canvas, ball) < 0) or (get_right_x_of_ball(canvas, ball) > canvas_width):
        return -1, 1
    elif (get_top_y_of_ball(canvas, ball) < 0):
        return 1, -1
    elif (get_bottom_y_of_ball(canvas, ball) > canvas_height):
        damage(canvas, ball)
        return 1, 1
    else:
        return 1,1

def check_collision(canvas, ball):
    coords = canvas.coords(ball)
    ball_x_1 = coords[0]
    ball_y_1 = coords[1]
    ball_x_2 = coords[2]
    ball_y_2 = coords[3]
    return canvas.find_overlapping(ball_x_1, ball_y_1, ball_x_2, ball_y_2)

# -------------------------------PADDLE---------------------------------
def check_mouse_is_in_game_area(canvas):
    left_limit = (PADDLE_WIDTH/2)
    right_limit = canvas.get_canvas_width() - (PADDLE_WIDTH / 2)
    x = canvas.get_mouse_x()
    canvas.update()
    return x < right_limit and x > left_limit

def movePaddle(canvas, paddle):
    mouse_x = canvas.get_mouse_x()
    y = canvas.get_canvas_height() - PADDLE_Y_OFFSET
    canvas.moveto(paddle, mouse_x - PADDLE_WIDTH/2, y)
    canvas.update()

def create_paddle(canvas):
    x = (canvas.get_canvas_width()/2) - (PADDLE_WIDTH/2)
    y = canvas.get_canvas_height() - PADDLE_Y_OFFSET
    paddle =  canvas.create_rectangle(x, y, x + PADDLE_WIDTH, y + PADDLE_HEIGHT)
    canvas.set_fill_color(paddle, "BLACK")
    return paddle

if __name__ == '__main__':
    main()