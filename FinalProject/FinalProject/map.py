import math

class Map:
    def __init__(self, canvas, map, mapWidth, mapHeight, depth, BRICK_SIZE):
        self.canvas = canvas
        self.map = map
        self.CANVAS_WIDTH = canvas.get_canvas_width()
        self.CANVAS_HEIGHT = canvas.get_canvas_height()
        self.BRICK_SIZE = BRICK_SIZE
        self.FOV = 3.14159 / 4.0
        self.created = False
        self.playerX = 8.0
        self.playerY = 8.0
        self.playerA = 0.0
        self.mapWidth = mapWidth
        self.mapHeight = mapHeight
        self.depth = depth
        self.walls = []

    def check_controls(self):
        # Controls
        # Handle CCW Rotation
        presses = self.canvas.get_new_key_presses()
        self.canvas.update()
        for key in presses:
            if key.keysym == 'a':
                self.created = False
                self.playerA += (0.1)
            elif key.keysym == 'd':
                self.created = False
                self.playerA -= (0.1)
            elif key.keysym == 'w':
                self.created = False
                self.playerX += math.sin(self.playerA) * 2.0
                self.playerY += math.cos(self.playerA) * 2.0
                if self.map[int(self.playerY) * self.mapWidth + int(self.playerX)] == '#':
                    self.playerX -= math.sin(self.playerA) * 2.0
                    self.playerY -= math.cos(self.playerA) * 2.0
            elif key.keysym == 's':
                self.created = False
                self.playerX -= math.sin(self.playerA) * 2.0
                self.playerY -= math.cos(self.playerA) * 2.0

                if self.map[int(self.playerY) * self.mapWidth + int(self.playerX)] == '#':
                    self.playerX += math.sin(self.playerA) * 2.0
                    self.playerY += math.cos(self.playerA) * 2.0

        self.canvas.update()

    def generate_map(self):
        self.check_controls()
        if not self.created:
            self.delete_all()
            self.canvas.update()
            for x in range(0, self.CANVAS_WIDTH, self.BRICK_SIZE):
                # Takes the player angle and tries to find out what's the starting angle for the field of view
                # and second part of this line is chopping it up into little bits so in this case 120 because that's the width of our screen
                rayAngle = (self.playerA - self.FOV / 2.0) + (float(x) / float(self.CANVAS_WIDTH)) * self.FOV

                # what is the distance from the player to the wall for that given angle
                distanceToWall = 0
                hitWall = False

                eyeX = math.sin(rayAngle)  # Unit vector for ray in player space
                eyeY = math.cos(rayAngle)

                while not hitWall and distanceToWall < self.depth:
                    distanceToWall += 0.1

                    # given distance in this case we want to extend our unit vector to the length that we're currently checkking
                    # for so this distance the wall is going to grow and therefore our unit vector is going to grow in the right direction
                    testX = int(self.playerX + eyeX + distanceToWall)
                    testY = int(self.playerY + eyeY + distanceToWall)

                    # Test if ray is out of bounds
                    if testX < 0 or testX >= self.mapWidth or testY < 0 or testY >= self.mapHeight:
                        hitWall = True  # Just set distance to maxiumum depth
                        distanceToWall = self.depth
                    else:
                        # we want to check cells individually on the map
                        # Ray is inbounds so tests to see if the ray cell is a wall block
                        if (self.map[testY * self.mapWidth + testX] == '#'):
                            hitWall = True

                # Calculate distance to celling and floor
                ceiling = float(self.CANVAS_HEIGHT / 2.0) - self.CANVAS_HEIGHT * (float(distanceToWall))
                floor = self.CANVAS_HEIGHT - ceiling  # just the mirror of the ceiling

                if distanceToWall <= self.depth / 4.0:
                    shade = "./sprites/brick.png "  # very close
                elif distanceToWall < self.depth / 3.0:
                    shade = "./sprites/shade_2.png"
                elif distanceToWall < self.depth / 2.0:
                    shade = "./sprites/shade_3.png"
                elif distanceToWall < self.depth:
                    shade = "./sprites/shade_4.png"
                else:
                    shade = "./sprites/foo.png"  # Too far away

                for y in range(0, self.CANVAS_HEIGHT, self.BRICK_SIZE):
                    if y < ceiling:
                        # canvas[y * CANVAS_WIDTH + x] = ' '
                        continue
                    elif y > ceiling and y <= floor:
                        wall = self.create_brick(self.CANVAS_WIDTH - x, y, self.BRICK_SIZE, self.BRICK_SIZE, shade)
                        self.canvas.update()
                        self.walls.append(wall)
                        # canvas[y * CANVAS_WIDTH + x] = '#'
                    else:
                        # canvas[y * CANVAS_WIDTH + x] = ' '
                        continue
            self.created = True

    def create_brick(self, x, y, width, height, shade):
        return self.canvas.create_image_with_size(x, y, width, height, shade)

    def delete_all(self):
        for wall in self.walls:
            self.canvas.delete(wall)
            self.canvas.update()
        self.walls.clear()