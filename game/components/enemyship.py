import pygame
import random
from pygame.sprite import Sprite

from game.utils.constants import ENEMY_1, ENEMY_1_UP , ENEMY_1_RIGHT , ENEMY_1_LEFT , SCREEN_HEIGHT , SCREEN_WIDTH

class EnemyShip(Sprite):
    def __init__(self):
        self.image_size = (130, 130)
        self.position = [450, 20]
        self.velocity_x = 30
        self.velocity_y = 15
        self.image = pygame.transform.scale(ENEMY_1, self.image_size)
        self.image_rect = self.image.get_rect()
        self.image_rect.x = self.position[0]
        self.image_rect.y = self.position[1]
        self.moving_x = True
        self.moving_y = False

    def update_x(self):
        if not self.moving_x:
            return
        
        self.image_rect.x += self.velocity_x
        
        if self.image_rect.right > SCREEN_WIDTH or self.image_rect.left < 0:
            self.velocity_x *= -1        
            
        if self.image_rect.x < 60:
            self.image = pygame.transform.scale(ENEMY_1_RIGHT, self.image_size)
            self.moving_x = False
            self.moving_y = True
            
        if self.image_rect.x > 920:
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
