"""
File: project.py
-----------------
This program is an empty program for your final project.  Update this comment
with a summary of your program!
"""

from graphics import Canvas
from winsound import PlaySound,SND_FILENAME,SND_ASYNC
import time
import threading

GUN_SPRITE = "./sprites/Gun.png"
GUN_WIDTH = 300
GUN_HEIGHT = 350

ENEMY_SPRITE = "./sprites/Enemy.png"
ENEMY_WIDTH = 300
ENEMY_HEIGHT = 300
ENEMY_HEALTH = 100

FIRE_RANGE = 500
DAMAGE_AMOUNT = 10
FIRE_SOUND = './sounds/fire.wav'

def main():
    canvas = Canvas(1440, 900)
    canvas.set_canvas_title("Final Project")

    gun = Gun(canvas, GUN_WIDTH, GUN_HEIGHT, 50)
    enemy = Enemy(canvas, ENEMY_WIDTH, ENEMY_HEIGHT, 100)
    player = Player(canvas, gun)

    while True:
        clicks = canvas.get_new_mouse_clicks()
        canvas.update()
        if len(clicks) > 0:
            player.shoot()
            enemy.check_for_bullet(player.fire_triangule)
            canvas.update()

    canvas.mainloop()

class Player:
    def __init__(self, canvas, gun):
        self.gun = gun
        self.canvas = canvas

    def shoot(self):
        if self.gun.ammo > 0:
            z = threading.Thread(target=self.fire_range(FIRE_RANGE), args=(FIRE_RANGE))
            z.start()
            y = threading.Thread(target=PlaySound, args=(FIRE_SOUND, SND_FILENAME | SND_ASYNC))
            y.start()
            x = threading.Thread(target=self.muzzle_flash())
            x.start()
            self.gun.ammo -= 1

    def muzzle_flash(self):
        muzzle = self.canvas.create_image_with_size(self.canvas.get_canvas_width() / 2 - 100,
                                                    self.canvas.get_canvas_height() - (self.gun.height + 100), 200, 200,
                                                    "./sprites/MuzzleFlash_1.png")
        self.canvas.lower_behind(muzzle, self.gun.image)
        self.canvas.update()
        time.sleep(0.3)
        self.canvas.delete(muzzle)
        self.canvas.update()

    def fire_range(self, width):
        triangule = self.canvas.create_image_with_size(self.canvas.get_canvas_width() / 2 - width/2,
                                                       0,
                                                       width, self.canvas.get_canvas_height() - self.gun.height,
                                                       "./sprites/triangule.png")
        self.fire_triangule = triangule
        self.canvas.update()
        time.sleep(1)
        self.canvas.delete(triangule)
        self.canvas.update()

class Enemy:
    def __init__(self, canvas, width, height, health):
        self.canvas = canvas
        self.health = health
        self.width = width
        self.height = height
        self.image = canvas.create_image_with_size(canvas.get_canvas_width()/2 - width/2, canvas.get_canvas_height()/2 - height, width, height, ENEMY_SPRITE)
        canvas.update()

    def take_damage(self, amount):
        self.health -= amount
        if self.health <= 0:
            self.die()

    def die(self):
        self.canvas.delete(self)
        self.canvas.update()

    def check_for_bullet(self, fire_triangule):
        coords = self.canvas.coords(self.image)

        collided_list = self.canvas.find_overlapping(coords[0], coords[1], coords[0] + self.width, coords[1] + self.height)
        for col in collided_list:
            if col is fire_triangule:
                self.take_damage(DAMAGE_AMOUNT)
                print(self.health)

class Gun:
    def __init__(self, canvas, width, height, ammo):
        self.canvas = canvas
        self.ammo = ammo
        self.width = width
        self.height = height
        self.image = canvas.create_image_with_size(canvas.get_canvas_width() / 2 - width / 2,
                                      canvas.get_canvas_height() - height, width, height,
                                      GUN_SPRITE)
        canvas.update()
    def get_coords(self):
        return self.canvas.coords(self)

if __name__ == '__main__':
    main()
