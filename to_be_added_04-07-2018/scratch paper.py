'''
Generate a new ball by pressing the middle button on the mouse(the wheel)
Each ball has a direction arrow to point toward the direction of its velocity
The size of each arrow is proportional to the size of each accompanying ball,
arrowsize = 1.2* Radius_of Ball

The upgraded features of this version are:

The best rectangle you can get for a sprite

self.rect = self.image.get_bounding_rect(min_alpha=1)

The scrolling of the surface on which the drawing it is done to a new location at ( dx, dy) from (0,0 )

 self.image.scroll(dx=int(SCREEN_WIDTH / 2), dy=int(SCREEN_HEIGHT / 2))


By moving the Surface to the center of the board,  one can generate each ball at that location:

self.pos = vec(int(SCREEN_WIDTH/2), int(SCREEN_HEIGHT/2))

and, therefor the velocity could be randomized in all directions random.randrange(-5, 5)


'''

import random

import pygame

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (0, 255, 0)
YELLOW = (255, 255, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
HOVERING = (255, 51, 255)
ORANGE = (255, 128, 0)
SCREEN_WIDTH = 720
SCREEN_HEIGHT = 480

vec = pygame.math.Vector2
size = [SCREEN_WIDTH, SCREEN_HEIGHT]


class Ball(pygame.sprite.Sprite):

    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.BALL_SIZE = random.randrange(20, 40)
        self.arrowsize = 1.25 * self.BALL_SIZE
        self.x = 25
        self.y = 25
        self.sweepx = 0
        self.sweepy = 0
        self.image = pygame.Surface((50, 50))

        self.image.set_colorkey(BLACK)  # black transparent
        pygame.draw.circle(self.image, RED, (25, 25), int(self.BALL_SIZE / 2), 2)  # red circle
        pygame.draw.polygon(self.image, YELLOW, (
            (25, 24), (self.arrowsize, 24), (self.arrowsize, 21), (5 + self.arrowsize, 25), (self.arrowsize, 29),
            (self.arrowsize, 26), (25, 26)), 0)
        self.image_orig = self.image.convert_alpha()
        self.image.scroll(dx=int(SCREEN_WIDTH / 2), dy=int(SCREEN_HEIGHT / 2))
        self.vel = vec(0.0, 0.0)
        self.direction = -90 + self.vel.angle_to(vec(0, 1))
        self.arrowsize = 1
        self.image = pygame.transform.rotozoom(self.image_orig, self.direction, self.arrowsize)
        self.rect = self.image_orig.get_rect()
        self.radius = self.BALL_SIZE / 2  # for collide check
        self.image = self.image_orig.copy()
        self.rect = self.image.get_bounding_rect(min_alpha=1)
        self.rect.center = (self.x, self.y)
        self.pos = vec(int(SCREEN_WIDTH / 2), int(SCREEN_HEIGHT / 2))
        self.acc = vec(float(0.0), float(0.0))
        self.change_x = random.randrange(-3, 2)
        self.change_y = random.randrange(-2, 1)
        self.vel = vec(self.change_x, self.change_y)
        self.direction = -90
        self.mass = 3.14 * self.BALL_SIZE * self.BALL_SIZE
        self.rot = random.randrange(0, 90)
        # The direction of the velocity vector
        self.direction = -90 + self.vel.angle_to(vec(0, 1))
        #  dir and norm
        self.dir = vec(1.0, 0.0).rotate(self.rot)
        self.norm = self.dir.rotate(90 - self.rot)
        self.rot_speed = -random.randrange(2, 8)
        self.last_update = pygame.time.get_ticks()

    def rotate(self):

        now = pygame.time.get_ticks()
        if now - self.last_update > 100:
            self.last_update = now
            self.rot = (self.rot + self.rot_speed) % 360
            new_image = pygame.transform.rotozoom(self.image_orig, self.direction, self.arrowsize)
            old_center = self.rect.center
            self.image = new_image
            self.rect = self.image.get_rect()
            self.rect.center = old_center

    def update(self):
        self.rotate()
        self.vel += self.acc
        self.pos += self.vel
        self.direction = -90 + self.vel.angle_to(vec(0, 1))

        self.pos += self.vel
        if self.pos[1] > SCREEN_HEIGHT - self.BALL_SIZE - 2 or self.pos[1] < self.BALL_SIZE:
            # using the reflect()
            self.vel = self.vel.reflect(vec(0, 1))
        if self.pos[0] > SCREEN_WIDTH - self.BALL_SIZE - 2 or self.pos[0] < self.BALL_SIZE:
            # using the reflect()
            self.vel = self.vel.reflect(vec(1, 0))

        self.rect.center = (self.pos[0], self.pos[1])


def main():
    pygame.init()
    # Set the height and width of the screen
    screen = pygame.display.set_mode(size)
    pygame.display.set_caption("Platforms")
    # Loop until the user clicks the close button.
    done = False
    # Used to manage how fast the screen updates
    clock = pygame.time.Clock()

    ballgroup = pygame.sprite.Group()
    allsprites = pygame.sprite.Group()
    ball_list = []

    while not done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
            elif event.type == pygame.MOUSEBUTTONDOWN:

                if event.button == 2:
                    ball = Ball()
                    ballgroup.add(ball)
                    allsprites.add(ball)
                    ball_list.append(ball)



            elif event.type == pygame.MOUSEBUTTONUP:
                if event.button == 2:
                    selected = None

        for ball1 in ball_list:

            for ball2 in ball_list:
                if ball2 == pygame.sprite.spritecollideany(ball1, ball_list, collided=None):
                    if ball2 == ball1:
                        continue
                    else:

                        v1i = ball1.vel
                        v2i = ball2.vel
                        m1 = 3.14 * ball1.BALL_SIZE ** 2
                        m2 = 3.14 * ball2.BALL_SIZE ** 2
                        ball1.vel = (m1 - m2) / (m1 + m2) * v1i + 2 * m2 / (m1 + m2) * v2i
                        ball2.vel = 2 * m1 / (m1 + m2) * v1i + (m2 - m1) / (m1 + m2) * v2i

        allsprites.update()
        screen.fill(BLACK)
        clock.tick(60)

        # Go ahead and update the screen with what we've drawn.
        allsprites.draw(screen)

        pygame.display.flip()
    # Close everything down
    pygame.quit()


if __name__ == "__main__":
    main()
