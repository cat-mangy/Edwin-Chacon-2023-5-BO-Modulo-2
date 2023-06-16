import pygame

from game.utils.constants import BG, ICON, SCREEN_HEIGHT, SCREEN_WIDTH, TITLE, FPS, DEFAULT_TYPE

from game.components.spaceship import SpaceShip

from game.components.spaceship import bullets

from game.components.enemy_ship import EnemyShip, BULLET_ENEMY , bullets_enemy

# Game tiene un "Spaceship" - Por lo general esto es iniciliazar un objeto Spaceship en el __init__

GAME_START_EVENT = pygame.USEREVENT + 1

class Game:
    def __init__(self):
        pygame.init()
        pygame.display.set_caption(TITLE)
        pygame.display.set_icon(ICON)
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        self.clock = pygame.time.Clock()
        self.playing = False  # variable de control para salir del ciclo
        self.game_speed = 10
        self.x_pos_bg = 0
        self.y_pos_bg = 0
        self.bullets = bullets
        self.bullets_enemy = bullets_enemy
        
        # Game tiene un "Spaceship"
        self.spaceship = SpaceShip()
        
        # Game tiene un "Enemyship"
        self.enemyship = EnemyShip()



    def run(self):
        # Game loop: events - update - draw
        self.playing = True
        
        if pygame.sprite.spritecollide(self.enemyship, bullets_enemy, True):
            self.playing = False
            print("¡La nave ha sido alcanzada! Fin del juego.")

        # while self.playing == True
        while self.playing: # Mientras el atributo playing (self.playing) sea true "repito"
            self.handle_events()
            self.update()
            self.draw()
            self.enemyship.shoot_enemy() 
        else:
            print("Something ocurred to quit the game!!!")
        pygame.display.quit()
        pygame.quit()
        

    def handle_events(self):
        # Para un "event" (es un elemento) en la lista (secuencia) que me retorna el metodo get()
        for event in pygame.event.get():
            # si el "event" type es igual a pygame.QUIT entonces cambiamos playing a False
            if event.type == pygame.QUIT:
                self.playing = False
                
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_SPACE:
                    self.spaceship.shoot()

    def update(self):
        # pass
        self.spaceship.update()
        self.enemyship.update()
        self.bullets.update()
        self.bullets_enemy.update()
        

    def draw(self):
        self.clock.tick(FPS)
        self.screen.fill((255, 255, 255))
        self.draw_background()


        # dibujamos el objeto en pantalla
        self.screen.blit(self.spaceship.image, self.spaceship.image_rect_s)
        self.screen.blit(self.enemyship.image, self.enemyship.image_rect)
        
        for bullet in bullets:
            self.screen.blit(bullet.image, bullet.image_rect)
            
        for bullet_enemy in bullets_enemy:
            self.screen.blit(bullet_enemy.image, bullet_enemy.image_rect)

        pygame.display.update()
        pygame.display.flip()

    def draw_background(self):
        image = pygame.transform.scale(BG, (SCREEN_WIDTH, SCREEN_HEIGHT))
        image_height = image.get_height()
        self.screen.blit(image, (self.x_pos_bg, self.y_pos_bg))
        self.screen.blit(image, (self.x_pos_bg, self.y_pos_bg - image_height))
        if self.y_pos_bg >= SCREEN_HEIGHT:
            self.screen.blit(image, (self.x_pos_bg, self.y_pos_bg - image_height))
            self.y_pos_bg = 0
        self.y_pos_bg += self.game_speed
