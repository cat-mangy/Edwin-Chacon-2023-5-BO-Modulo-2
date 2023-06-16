import pygame
import time
from pygame.sprite import Sprite, Group

from game.utils.constants import ENEMY_1_RIGHT, ENEMY_1_LEFT, SCREEN_HEIGHT, SCREEN_WIDTH, BULLET_ENEMY

class EnemyShip(Sprite):
    def __init__(self):
        super().__init__()
        self.image_size = (130, 130)
        self.position = [70, 0]
        self.velocity_x = 15
        self.velocity_y = 15
        self.change_images = False
        self.image = pygame.transform.scale(ENEMY_1_RIGHT, self.image_size)
        self.image_rect = self.image.get_rect()
        self.rect = self.image.get_rect()
        self.image_rect.x = self.position[0]
        self.image_rect.y = self.position[1]
        self.image_rect.centerx = SCREEN_HEIGHT // 2
        self.change_images = True
        self.moving_x = True
        self.moving_y = False
        self.shooting = False
        self.shoot_interval = 0.5  # Intervalo de tiempo entre disparos en segundos
        self.last_shot_time = 0.0  # Tiempo del último disparo

    def update_x(self):
        if not self.moving_x:
            return
        
        self.image_rect.x += self.velocity_x
        
        if self.image_rect.right > SCREEN_WIDTH or self.image_rect.left < 0:
            self.velocity_x *= -1        
            
        if self.image_rect.x < 60:
            if self.change_images:
                self.image = pygame.transform.scale(ENEMY_1_RIGHT, self.image_size)  
                   
            self.moving_x = False
            self.moving_y = True
            
        if self.image_rect.x > 920:
            if self.change_images:
                self.image = pygame.transform.scale(ENEMY_1_LEFT, self.image_size)  
                   
            self.moving_x = False
            self.moving_y = True

    def update_y(self):
        if not self.moving_y:
            return

        self.image_rect.y += self.velocity_y
        
        if self.image_rect.bottom > SCREEN_HEIGHT or self.image_rect.top < 0:
            self.velocity_y *= -1
            self.moving_x = True
            self.moving_y = False
            
    def update(self):
        self.update_x()
        self.update_y()
        
    def shoot_enemy(self):
        for i in range(8):
            if self.moving_y:
                current_time = time.time()
                if current_time - self.last_shot_time >= self.shoot_interval:
                    bullet_enemy = Bullet_Enemy(self.image_rect.centerx, self.image_rect.top)
                    bullets_enemy.add(bullet_enemy)
                    self.last_shot_time = current_time
bullets_enemy = pygame.sprite.Group()

class Bullet_Enemy(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image_size = (60, 60)
        self.image = pygame.transform.scale(BULLET_ENEMY, self.image_size)
        self.image_rect = self.image.get_rect()
        self.image_rect.centerx = x
        self.image_rect.y = y
        self.speed_x = self.speed_x = 15 if self.image_rect.x <= 60 else -15 if self.image_rect.x >= 920 else 15

    def update(self):
        self.image_rect.x += self.speed_x
        if self.image_rect.left < 0:
            self.kill()

