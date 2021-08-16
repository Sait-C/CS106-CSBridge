"""
File: project.py
-----------------
This program is an empty program for your final project.  Update this comment
with a summary of your program!
"""

from graphics import Canvas


GUN_WIDTH = 300
GUN_HEIGHT = 350

ENEMY_WIDTH = 300
ENEMY_HEIGHT = 300
ENEMY_HEALTH = 100

def main():
    canvas = Canvas(1440, 900)
    canvas.set_canvas_title("Final Project")

    gun = Gun(canvas, GUN_WIDTH, GUN_HEIGHT)
    enemy = Enemy(canvas, ENEMY_WIDTH, ENEMY_HEIGHT, 100)

    canvas.mainloop()


class Enemy:
    def __init__(self, canvas, width, height, health):
        self.canvas = canvas
        self.health = health
        canvas.create_image_with_size(canvas.get_canvas_width()/2 - width/2, canvas.get_canvas_height()/2 - height, width, height, "./sprites/Enemy.png")
        canvas.update()

    def take_damage(self, amount):
        self.health -= amount
        if self.health <= 0:
            self.die()

    def die(self):
        self.canvas.delete(self)
        self.canvas.update()

class Gun:
    def __init__(self, canvas, width, height):
        self.canvas = canvas
        canvas.create_image_with_size(canvas.get_canvas_width() / 2 - width / 2,
                                      canvas.get_canvas_height() - height, width, height,
                                      "./sprites/Gun.png")
        canvas.update()
    def get_coords(self):
        return self.canvas.coords(self)

if __name__ == '__main__':
    main()
