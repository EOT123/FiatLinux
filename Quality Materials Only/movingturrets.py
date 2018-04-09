# Turret rotation


import numpy as np
import pygame as pg

vec = pg.math.Vector2

# colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)

# Settings
PLAYER_ACC = 0.5
PLAYER_FRICTION_GROUND = -0.12
PLAYER_FRICTION_AIR = 0.12


# Functions

# Classes
class Player(pg.sprite.Sprite):
    def __init__(self):
        pg.sprite.Sprite.__init__(self)
        self.image = pg.Surface((30, 40))
        self.image.fill(GREEN)
        self.rect = self.image.get_rect()
        self.rect.center = (WIDTH / 2, HEIGHT - 100)
        self.pos = vec(WIDTH / 2, HEIGHT - 100)
        self.vel = vec(0, 0)
        self.acc = vec(0, 0)

    def update(self):
        self.acc = vec(0, 2)

        keys = pg.key.get_pressed()
        if keys[pg.K_LEFT]:
            self.acc.x = - PLAYER_ACC
        elif keys[pg.K_RIGHT]:
            self.acc.x = PLAYER_ACC
        elif keys[pg.K_UP]:
            self.acc.y = -2
        # Apply friction for horizontal motion
        self.acc.x += self.vel.x * PLAYER_FRICTION_GROUND

        self.acc.y += -self.vel.y * PLAYER_FRICTION_AIR

        # The motion.s equations
        self.vel.x += self.acc.x
        self.vel.y += self.acc.y
        self.pos.x += self.vel.x + 0.5 * self.acc.x
        # if self.acc.y <= 0:

        self.pos.y += self.vel.y + self.acc.y
        if self.pos.x < 0:
            self.pos.x = WIDTH
        if self.pos.x > WIDTH:
            self.pos.x = 0
        if self.pos.y < 0:
            self.vel.y *= -1
        if self.pos.y >= HEIGHT - 100:
            self.pos.y = HEIGHT - 100
        self.rect.center = self.pos


class Turret(pg.sprite.Sprite):
    def __init__(self, x, y):
        pg.sprite.Sprite.__init__(self)
        self.image_orig = pg.Surface((20, 80))
        self.image_orig.fill(YELLOW)
        self.image = self.image_orig.copy()
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)
        self.rot = 0
        self.last_update = pg.time.get_ticks()

    def rotate(self):
        now = pg.time.get_ticks()
        if now - self.last_update > 100:
            self.last_update = now
            self.rot = self.angle()
            new_image = pg.transform.rotozoom(self.image_orig, self.rot, 1)
            old_center = self.rect.center
            self.image = new_image
            self.rect = self.image.get_rect()
            self.rect.center = old_center

    def angle(self):
        x_change = self.rect.centerx - player.rect.centerx
        y_change = self.rect.centery - player.rect.centery
        return round(np.degrees(np.arctan(x_change / y_change)))

    def update(self):
        self.rotate()


pg.init()

# screen
WIDTH = 468
HEIGHT = 600
FPS = 60

size = (WIDTH, HEIGHT)
screen = pg.display.set_mode(size)
pg.display.set_caption("Rotation")

running = True
clock = pg.time.Clock()

# The groups for sprites
all_sprites = pg.sprite.Group()
player = Player()
all_sprites.add(player)
turrets = pg.sprite.Group()
turret1 = Turret(WIDTH / 2, 20)
turret2 = Turret(40, HEIGHT / 2)
turret3 = Turret(WIDTH - 40, HEIGHT / 2)
turrets.add(turret1)
turrets.add(turret2)
turrets.add(turret3)
all_sprites.add(turret1)
all_sprites.add(turret2)
all_sprites.add(turret3)

# The main loop

while running:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False

    clock.tick(FPS)

    # all sprite update

    all_sprites.update()

    # screen definition

    screen.fill(BLACK)

    # Draw

    all_sprites.draw(screen)

    pg.display.flip()
pg.quit()
