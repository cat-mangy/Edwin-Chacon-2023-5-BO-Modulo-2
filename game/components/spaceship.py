import pygame
from pygame.sprite import Sprite

from game.utils.constants import SPACESHIP,SCREEN_HEIGHT,SCREEN_WIDTH

# casi Todo en pygame es un objeto
# Un personaje en mi juego es un objeto (instancia de algo)
# La nave (spaceship) es un personaje => necesito una clase


# SpaceShip es una clase derivada (hija) de Sprite

# spaceship tiene una "imagen"
class SpaceShip(Sprite):
    
    def __init__(self):
        self.image_size = (60, 60)
        self.position = [500,270]
        self.velocity = 15
        self.image = pygame.transform.scale(SPACESHIP, self.image_size)
        self.image_rect = self.image.get_rect()
        self.image_rect.x = self.position[0]
        self.image_rect.y = self.position[1]

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
            self.position[0] = SCREEN_WIDTH - 1
        if self.position[0] >= SCREEN_WIDTH:
            self.position[0] = 0
            
        if self.position[1] <= 0:
            self.position[1] = SCREEN_HEIGHT - 1
        if self.position[1] >= SCREEN_HEIGHT:
            self.position[1] = 0
            
        self.image_rect.x = self.position[0]
        self.image_rect.y = self.position[1]