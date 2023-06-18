import pygame
import time
from pygame.sprite import Sprite

from game.utils.constants import ENEMY_1_RIGHT, ENEMY_1_LEFT, SCREEN_HEIGHT, SCREEN_WIDTH, BULLET_ENEMY

bullets_enemy = pygame.sprite.Group()


class EnemyShip(Sprite):
    def __init__(self):
        super().__init__()
        self.image_size = (130, 130)
        self.position = [70, 0]
        self.velocity_x = 15
        self.velocity_y = 20
        self.change_images = False
        self.image = pygame.transform.scale(ENEMY_1_RIGHT, self.image_size)
        self.rect = self.image.get_rect()
        self.rect.x = self.position[0]
        self.rect.y = self.position[1] 
        self.rect.centerx = SCREEN_HEIGHT // 2
        self.change_images = True
        self.moving_x = True
        self.moving_y = False
        self.shooting = False
        self.shoot_interval = 0.3
        self.last_shot_time = 0.0 
        self.lives = 5

    def update_x(self):
        if not self.moving_x:
            return
        
        self.rect.x += self.velocity_x
        
        if self.rect.right > SCREEN_WIDTH or self.rect.left < 0:
            self.velocity_x *= -1        
            
        if self.rect.x < 60:
            if self.change_images:
                self.image = pygame.transform.scale(ENEMY_1_RIGHT, self.image_size)  
                   
            self.moving_x = False
            self.moving_y = True
            
        if self.rect.x > 920:
            if self.change_images:
                self.image = pygame.transform.scale(ENEMY_1_LEFT, self.image_size)  
                   
            self.moving_x = False
            self.moving_y = True

    def update_y(self):
        if not self.moving_y:
            return

        self.rect.y += self.velocity_y
        
        if self.rect.bottom > SCREEN_HEIGHT or self.rect.top < 0:
            self.velocity_y *= -1
            self.moving_x = True
            self.moving_y = False
            
    def update(self):
        self.update_x()
        self.update_y()

    def get_hit(self):
        self.lives -= 1
        if self.lives <= 0:
            self.kill()
        
    def shoot_enemy(self):
            if self.moving_y:
                current_time = time.time()
                if current_time - self.last_shot_time >= self.shoot_interval:
                    bullet_enemy = Bullet_Enemy(self.rect.centerx, self.rect.top)
                    bullets_enemy.add(bullet_enemy)
                    self.last_shot_time = current_time


class Bullet_Enemy(Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image_size = (30, 30)
        self.image = pygame.transform.scale(BULLET_ENEMY, self.image_size)
        self.rect = self.image.get_rect()
        self.rect.centerx = x
        self.rect.y = y
        self.speed_x = 15 if self.rect.x <= 60 else -15 if self.rect.x >= 920 else 15

    def update(self):
        self.rect.x += self.speed_x
        if self.rect.left < 0:
            self.kill()

