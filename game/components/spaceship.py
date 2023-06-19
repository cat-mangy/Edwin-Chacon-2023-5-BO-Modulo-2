import pygame
import threading
import time

from pygame.sprite import Sprite, Group

from game.utils.constants import SPACESHIP, SPACESHIP_SHIELD , BURST ,BULLET, SCREEN_HEIGHT, SCREEN_WIDTH

pygame.init()

bullets = pygame.sprite.Group()

class SpaceShip(Sprite):
    def __init__(self):
        super().__init__()
        self.image_size = (60, 60)
        self.position = [500, 270]
        self.velocity = 15
        self.image = pygame.transform.scale(SPACESHIP, self.image_size)
        self.rect = self.image.get_rect()  
        self.rect.x = self.position[0]
        self.rect.y = self.position[1]
        self.rect.centerx = SCREEN_WIDTH // 2
        self.lives = 3
        self.time_hit = 0 
        self.hit_duration = 500
        self.shield_active = False
        self.last_shield_activation = 0
        self.shield_cooldown = 15

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

        self.rect.x = self.position[0]  
        self.rect.y = self.position[1] 

        if pygame.time.get_ticks() - self.time_hit < self.hit_duration:
            self.image = pygame.transform.scale(BURST, self.image_size)
        else:
            self.image = pygame.transform.scale(SPACESHIP, self.image_size)
            
        if self.shield_active:
            self.image = pygame.transform.scale(SPACESHIP_SHIELD, self.image_size)

        
    def get_hit(self):
        self.lives -= 1
        self.time_hit = pygame.time.get_ticks()

        if self.lives <= 0:
            self.kill()

    def get_lives(self):
        return self.lives

    def shoot(self):
        bullet = Bullet(self.rect.centerx, self.rect.top)
        bullets.add(bullet)
    
    def shield(self):
        current_time = time.time()
        if not self.shield_active and current_time - self.last_shield_activation >= self.shield_cooldown:
            self.lives = float('inf')
            self.shield_active = True
            self.last_shield_activation = current_time

            # Desactivar el escudo después de 5 segundos
            threading.Timer(3.5, self.no_shield).start()

    def no_shield(self):
        self.lives = 2
        self.shield_active = False

class Bullet(Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image_size = (60, 60)
        self.image = pygame.transform.scale(BULLET, self.image_size)
        self.rect = self.image.get_rect()
        self.rect.centerx = x
        self.rect.y = y
        self.speed_y = -15

    def update(self):
        self.rect.y += self.speed_y
        if self.rect.bottom < 0:
            self.kill()
