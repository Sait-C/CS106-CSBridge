"""
File: project.py
-----------------
This program is an empty program for your final project.  Update this comment
with a summary of your program!
"""

from graphics import Canvas
from winsound import PlaySound,SND_FILENAME,SND_ASYNC
import time
from map import Map

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

MAP = f"################" \
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

def main():
    global t
    canvas = Canvas(1440, 900)
    canvas.set_canvas_title("Final Project")

    map = Map(canvas, MAP, 16, 16, 16, 100)
    map.generate_map()
    gun = Gun(canvas, GUN_WIDTH, GUN_HEIGHT, 50)
    enemy = Enemy(canvas, ENEMY_WIDTH, ENEMY_HEIGHT, 100)
    player = Player(canvas, gun)



    while True:
        clicks = canvas.get_new_mouse_clicks()
        canvas.update()
        if len(clicks) > 0:
            # this functions must work asynchoronously
            player.shoot()
            enemy.take_damage(DAMAGE_AMOUNT) #this functions is temporary
            #enemy.check_for_bullet(player.fire_triangule)
            canvas.update()
        map.generate_map()
        canvas.update()
        canvas.raise_to_front(gun.image)
        canvas.raise_to_front(enemy.image)
        canvas.update()
    canvas.mainloop()

class Player:
    def __init__(self, canvas, gun):
        self.gun = gun
        self.canvas = canvas
        self.fire_triangule = None

    def shoot(self):
        if self.gun.ammo > 0:
            self.fire_range(FIRE_RANGE)
            self.muzzle_flash()
            self.play_sound(FIRE_SOUND)
            self.gun.ammo -= 1

    def play_sound(self, sound):
       PlaySound(sound, SND_FILENAME | SND_ASYNC)

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
    def __init__(self, canvas, width, height, max_health):
        self.canvas = canvas
        self.max_health = max_health
        self.width = width
        self.height = height
        self.image = self.creeate_image(width, height)
        self.current_health = max_health
        self.dead = False
        canvas.update()


    def creeate_image(self, width, height):
        return self.canvas.create_image_with_size(self.canvas.get_canvas_width()/2 - width/2, self.canvas.get_canvas_height()/2 - height, width, height, ENEMY_SPRITE)

    def take_damage(self, amount):
        if not self.dead:
            self.current_health -= amount
            print(self.current_health)
            if self.current_health <= 0:
                self.die()
                return
            self.canvas.delete(self.image)
            damage_count = (self.max_health - self.current_health)/amount
            self.image = self.creeate_image(self.width-(30 * int(damage_count)), self.height-(30 * int(damage_count)))
            self.canvas.update()


    def die(self):
        self.canvas.delete(self.image)
        self.canvas.update()
        self.dead = True

    def check_for_bullet(self, fire_triangule):
        if not self.dead:
            coords = self.canvas.coords(self.image)

            collided_list = self.canvas.find_overlapping(coords[0], coords[1], coords[0] + self.width, coords[1] + self.height)
            for col in collided_list:
                if col is fire_triangule:
                    self.take_damage(DAMAGE_AMOUNT)
                    print(self.current_health)

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
