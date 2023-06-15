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
        self.image_rect = self.image.get_rect()
        self.image_rect.x = self.position[0]
        self.image_rect.y = self.position[1]
        self.image_rect.centerx = SCREEN_WIDTH // 2

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
            
        if keystate[pygame.K_SPACE]:
            BulletManager()

        if self.position[0] <= 0:
            self.position[0] = SCREEN_WIDTH - 1
        if self.position[0] >= SCREEN_WIDTH:
            self.position[0] = 0

        if self.position[1] <= 0:
            self.position[1] = SCREEN_HEIGHT - 1
        if self.position[1] >= SCREEN_HEIGHT:
            self.position[1] = 0
            
        

        self.image_rect.x = self.position[0]
        self.image_rect.y = self.position[1]

    def shoot(self):
        bullet = Bullet(self.image_rect.centerx, self.image_rect.top)
        bullets.add(bullet)


class Bullet(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image_size = (60, 60)
        self.image = pygame.transform.scale(BULLET, self.image_size)
        self.image_rect = self.image.get_rect()
        self.image_rect.centerx = x
        self.image_rect.y = y
        self.speed_y = -10

    def update(self):
        self.image_rect.y += self.speed_y
        if self.image_rect.bottom < 0:
            self.kill()

bullets = pygame.sprite.Group()

class BulletManager:
    def __init__(self):
        self.bullets = []
        self.enemy_bullets = []

    def update(self, game):
        for bullet in self.enemy_bullets:
            bullet.update(self.enemy_bullets)

            if bullet.rect.colliderect(game.player.rect) and bullet.owner == 'enemy':
                self.enemy_bullets.remove(bullet)
                game.playing = False
                pygame.time.delay(1000)
                break
    
    def draw(self,screen):
        for bullet in self.enemy_bullets:
            bullet.draw(screen)

    def add_bullet(self, bullet):
        if bullet.owner == 'enemy' and len(self.enemy_bullets) < 1:
            self.enemy_bullets.append(bullet)
