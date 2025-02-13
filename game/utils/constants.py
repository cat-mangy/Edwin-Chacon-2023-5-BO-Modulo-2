import pygame
import os

# Global Constants
TITLE = "Spaceships Game"
SCREEN_HEIGHT = 600
SCREEN_WIDTH = 1100
FPS = 30
IMG_DIR = os.path.join(os.path.dirname(__file__), "..", "assets")

# Assets Constants
ICON = pygame.image.load(os.path.join(IMG_DIR, "Spaceship/spaceship.png"))

SHIELD = pygame.image.load(os.path.join(IMG_DIR, 'Other/shield.png'))

BG = pygame.image.load(os.path.join(IMG_DIR, 'Other/Track.png'))

HEART = pygame.image.load(os.path.join(IMG_DIR, "corazon\corazon.png"))
HEART = pygame.transform.scale(HEART, (40, 40))

HEART_BAD = pygame.image.load(os.path.join(IMG_DIR, "corazon/corazon_villano.png"))
HEART_BAD = pygame.transform.scale(HEART_BAD, (43, 43))

DEATH = pygame.image.load(os.path.join(IMG_DIR, "widow\calavera.png"))
DEATH = pygame.transform.scale(DEATH, (40, 40))

WIN = pygame.image.load(os.path.join(IMG_DIR, "widow\Trofeo.png"))
WIN = pygame.transform.scale(WIN, (40, 40))

DEFAULT_TYPE = "default"
SHIELD_TYPE = 'shield'

SPACESHIP = pygame.image.load(os.path.join(IMG_DIR, "Spaceship/spaceship.png"))
SPACESHIP_SHIELD = pygame.image.load(os.path.join(IMG_DIR, "Spaceship/spaceship_shield.png"))
BULLET = pygame.image.load(os.path.join(IMG_DIR, "Bullet/bullet_3.png"))

BULLET_ENEMY = pygame.image.load(os.path.join(IMG_DIR, "Bullet/bullet-2.png"))
BULLET_ENEMY_2 = pygame.image.load(os.path.join(IMG_DIR, "Bullet/bullet-1.png"))

ENEMY_1 = pygame.image.load(os.path.join(IMG_DIR, "Enemy/enemy_1.png"))
ENEMY_1_UP = pygame.image.load(os.path.join(IMG_DIR, "Enemy/enemy_1_up.png"))
ENEMY_1_RIGHT = pygame.image.load(os.path.join(IMG_DIR, "Enemy/enemy_1_right.png"))
ENEMY_1_LEFT = pygame.image.load(os.path.join(IMG_DIR, "Enemy/enemy_1_left.png"))

BURST = pygame.image.load(os.path.join(IMG_DIR, "Burst/burst.png"))

GAME_OVER = pygame.image.load(os.path.join(IMG_DIR, "widow\Sin título-4.png"))

FONT_STYLE = 'freesansbold.ttf'
