import pygame
from pygame.sprite import Sprite, Group

from game.utils.constants import SPACESHIP, BULLET, SCREEN_HEIGHT, SCREEN_WIDTH

pygame.init()

# Definir constantes y clases

# ... Código de las clases SpaceShip y Bullet ...

class SpaceShip(Sprite):
    def __init__(self):
        super().__init__()
        self.image_size = (60, 60)
        self.position = [500, 270]
        self.velocity = 15
        self.image = pygame.transform.scale(SPACESHIP, self.image_size)
        self.image_rect_s = self.image.get_rect()
        self.image_rect_s.x = self.position[0]
        self.image_rect_s.y = self.position[1]
        self.image_rect_s.centerx = SCREEN_WIDTH // 2

    def update(self):
        keystate = pygame.key.get_pressed()

        if keystate[pygame.K_LEFT]:
            self.position[0] -= self.velocity

        if keystate[pygame.K_RIGHT]:
            self.position[0] += self.velocity

        if keystate[pygame.K_UP]:
            self.position[1] -= self.velocity

        if keystate[pygame.K_DOWN]:
            self.position[1] += self.velocity

        if self.position[0] <= 0:
            self.position[0] = 0
        if self.position[0] >= 1045:
            self.position[0] = 1045

        if self.position[1] <= 0:
            self.position[1] = 0
        if self.position[1] >= 540:
            self.position[1] = 540

        self.image_rect_s.x = self.position[0]
        self.image_rect_s.y = self.position[1]
        

    def shoot(self):
        bullet = Bullet(self.image_rect_s.centerx, self.image_rect_s.top)
        bullets.add(bullet)

bullets = pygame.sprite.Group()

class Bullet(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image_size = (60, 60)
        self.image = pygame.transform.scale(BULLET, self.image_size)
        self.image_rect = self.image.get_rect()
        self.image_rect.centerx = x
        self.image_rect.y = y
        self.speed_y = -15

    def update(self):
        self.image_rect.y += self.speed_y
        if self.image_rect.bottom < 0:
            self.kill()

