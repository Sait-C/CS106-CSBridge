from graphics import Canvas
import math

CANVAS_WIDTH = 920
CANVAS_HEIGHT = 840

BRICK_SIZE = 100

FOV = 3.14159 / 4.0

def main():
    canvas = Canvas(CANVAS_WIDTH, CANVAS_HEIGHT)
    canvas.set_canvas_title("Final Project")

    playerX = 8.0
    playerY = 8.0
    playerA = 0.0

    mapHeight = 16
    mapWidth = 16
    depth = 16.0 #because our map size is 16

    map = f"################" \
          f"#              #" \
          f"#              #" \
          f"#              #" \
          f"#              #" \
          f"#              #" \
          f"#              #" \
          f"#              #" \
          f"#              #" \
          f"#              #" \
          f"#              #" \
          f"#              #" \
          f"#              #" \
          f"#              #" \
          f"#              #" \
          f"################" \

    created = False
    walls = []
    # Game Loop
    while True:
        # Controls
        # Handle CCW Rotation
        presses = canvas.get_new_key_presses()
        canvas.update()
        for key in presses:
            if key.keysym == 'a':
                created = False
                playerA += (0.1)
            elif key.keysym == 'd':
                created = False
                playerA -= (0.1)
            elif key.keysym == 'w':
                created = False
                playerX += math.sin(playerA) * 2.0
                playerY += math.cos(playerA) * 2.0
                if map[int(playerY) * mapWidth + int(playerX)] == '#':
                    playerX -= math.sin(playerA) * 2.0
                    playerY -= math.cos(playerA) * 2.0
            elif key.keysym == 's':
                created = False
                playerX -= math.sin(playerA) * 2.0
                playerY -= math.cos(playerA) * 2.0

                if map[int(playerY) * mapWidth + int(playerX)] == '#':
                    playerX += math.sin(playerA) * 2.0
                    playerY += math.cos(playerA) * 2.0

        canvas.update()
        if not created:
            canvas.delete_all()
            canvas.update()
            for x in range(0, CANVAS_WIDTH, BRICK_SIZE):
                # Takes the player angle and tries to find out what's the starting angle for the field of view
                # and second part of this line is chopping it up into little bits so in this case 120 because that's the width of our screen
                rayAngle = (playerA - FOV / 2.0) + (float(x) / float(CANVAS_WIDTH)) * FOV

                # what is the distance from the player to the wall for that given angle
                distanceToWall = 0
                hitWall = False
                # boundary is it the edge of the cell
                boundary = False

                eyeX = math.sin(rayAngle) # Unit vector for ray in player space
                eyeY = math.cos(rayAngle)

                while not hitWall and distanceToWall < depth:
                    distanceToWall += 0.1

                    # given distance in this case we want to extend our unit vector to the length that we're currently checkking
                    # for so this distance the wall is going to grow and therefore our unit vector is going to grow in the right direction
                    testX = int(playerX + eyeX + distanceToWall)
                    testY = int(playerY + eyeY + distanceToWall)


                    # Test if ray is out of bounds
                    if testX < 0 or testX >= mapWidth or testY < 0 or testY >= mapHeight:
                        hitWall = True # Just set distance to maxiumum depth
                        distanceToWall = depth
                    else:
                        # we want to check cells individually on the map
                        # Ray is inbounds so tests to see if the ray cell is a wall block
                        if (map[testY * mapWidth + testX] == '#'):
                            hitWall = True

                # Calculate distance to celling and floor
                ceiling = float(CANVAS_HEIGHT / 2.0) - CANVAS_HEIGHT * (float(distanceToWall))
                floor = CANVAS_HEIGHT - ceiling # just the mirror of the ceiling

                shade = ""
                if distanceToWall <= depth / 4.0: shade = "./sprites/brick.png "# very close
                elif distanceToWall < depth / 3.0: shade = "./sprites/shade_2.png"
                elif distanceToWall < depth / 2.0: shade = "./sprites/shade_3.png"
                elif distanceToWall < depth: shade = "./sprites/shade_4.png"
                else:                        shade = "./sprites/foo.png"          # Too far away


                for y in range(0, CANVAS_HEIGHT, BRICK_SIZE):
                    if y < ceiling:
                        #canvas[y * CANVAS_WIDTH + x] = ' '
                        continue
                    elif y > ceiling and y <= floor:
                        wall = create_brick(canvas, CANVAS_WIDTH - x, y, BRICK_SIZE, BRICK_SIZE, shade)
                        canvas.update()
                        walls.append(wall)

                        #canvas[y * CANVAS_WIDTH + x] = '#'
                    else:
                        # canvas[y * CANVAS_WIDTH + x] = ' '
                        continue
            created = True
    canvas.mainloop()


def create_brick(canvas, x, y, width, height, shade):
    canvas.create_image_with_size(x, y, width, height, shade)


if __name__ == '__main__':
    main()