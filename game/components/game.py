import pygame
import os

from game.utils.constants import BG, ICON, SCREEN_HEIGHT, SCREEN_WIDTH, FPS , HEART, HEART_BAD , DEATH, WIN , IMG_DIR
from game.components.spaceship import SpaceShip, bullets
from game.components.enemy_ship import EnemyShip, bullets_enemy
from game.components.boton import Button

class Game:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        self.clock = pygame.time.Clock()
        self.playing = False
        self.game_speed = 10
        self.x_pos_bg = 0
        self.y_pos_bg = 0
        self.bullets = bullets
        self.bullets_enemy = bullets_enemy
        self.spaceship = SpaceShip()
        self.enemyship = EnemyShip()
        self.restart_button = Button((255, 255, 255), SCREEN_WIDTH / 2 - 100, SCREEN_HEIGHT / 2 + 100, 200, 50, 'Reset')
        self.player_deaths = 0
        self.player_wins = 0
        self.font = pygame.font.Font(None, 32)
        self.death = DEATH
        self.win = WIN
    

    def show_game_over_screen(self):
        game_over_image = pygame.image.load(os.path.join(IMG_DIR, "widow\Sin título-4.png"))
        game_over_image = pygame.transform.scale(game_over_image, (300, 200))  

        image_rect = game_over_image.get_rect()
        image_rect.center = (SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 - 150)

        self.screen.blit(game_over_image, image_rect)
        pygame.display.flip()  

        run = True
        while run:
            icon_x = SCREEN_WIDTH / 2 - self.death.get_width()
            icon_y = SCREEN_HEIGHT / 2 
            self.screen.blit(self.death, (icon_x, icon_y))
            death_text = self.font.render(str(self.player_deaths), True, (255, 255, 255))
            text_x = icon_x + self.death.get_width() + 10
            text_y = icon_y + 10
            self.screen.blit(death_text, (text_x, text_y))
            self.restart_button.draw(self.screen, (0, 0, 0))
            pygame.display.flip()

            for event in pygame.event.get():
                pos = pygame.mouse.get_pos()
                if event.type == pygame.QUIT:
                    run = False
                    pygame.quit()
                    quit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if self.restart_button.is_over(pos):
                        self.restart_game()

    def show_game_win_screen(self):
        game_win_image = pygame.image.load(os.path.join(IMG_DIR, "widow\Sin título-6.png")) 
        game_win_image = pygame.transform.scale(game_win_image, (300, 200))  

        image_rect = game_win_image.get_rect()
        image_rect.center = (SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 - 150)

        self.screen.blit(game_win_image, image_rect)
        pygame.display.flip()  

        run = True
        while run:
            self.screen.blit(game_win_image, image_rect)
            death_text = self.font.render(str(self.player_wins), True, (255, 255, 255))
            icon_x = SCREEN_WIDTH // 2 - self.win.get_width()
            icon_y = SCREEN_HEIGHT // 2 
            self.screen.blit(self.win, (icon_x, icon_y))
            text_x = icon_x + self.win.get_width() + 10 
            text_y = icon_y + 10
            self.screen.blit(death_text, (text_x, text_y))
            self.restart_button.draw(self.screen, (0, 0, 0))
            pygame.display.flip()

            for event in pygame.event.get():
                pos = pygame.mouse.get_pos()
                if event.type == pygame.QUIT:
                    run = False
                    pygame.quit()
                    quit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if self.restart_button.is_over(pos):
                        print('Clicked the button')
                        self.restart_game()

        
    def restart_game(self):
        self.spaceship = SpaceShip()
        self.enemyship = EnemyShip()
        self.run()


    def check_collisions(self):
        if pygame.sprite.spritecollide(self.spaceship, bullets_enemy, True):
            self.spaceship.get_hit()
            if self.spaceship.lives <= 0:
                self.player_deaths += 1  
                self.show_game_over_screen()

        if pygame.sprite.spritecollide(self.enemyship, bullets, True):
            self.enemyship.get_hit()
            if self.enemyship.lives <= 0:
                self.player_wins +=1
                self.show_game_win_screen()

        enemyship_group = pygame.sprite.GroupSingle(self.enemyship)

        if pygame.sprite.spritecollide(self.spaceship, enemyship_group, False):
            self.spaceship.get_hit()


    def update(self):
        self.spaceship.update()
        self.enemyship.update()
        self.bullets.update()
        self.bullets_enemy.update()
        self.check_collisions()

    def run(self):
        self.playing = True
        while self.playing:
            self.handle_events()
            self.update()
            self.draw()
            self.enemyship.shoot_enemy()
        else:
            pass
        pygame.display.quit()
        pygame.quit()

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.playing = False
                
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_SPACE:
                    self.spaceship.shoot()
                    
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_x:
                    self.spaceship.shield()

    def draw(self):
        self.clock.tick(FPS)
        self.screen.fill((255, 255, 255))
        self.draw_background()
        self.screen.blit(self.spaceship.image, self.spaceship.rect)
        self.screen.blit(self.enemyship.image, self.enemyship.rect)
        self.screen.blit(HEART, (10, 10))
        self.screen.blit(HEART_BAD, (1046, 10))
        for bullet in bullets:
            self.screen.blit(bullet.image, bullet.rect)
        
        for bullet_enemy in bullets_enemy:
            self.screen.blit(bullet_enemy.image, bullet_enemy.rect)

       
        font = pygame.font.Font(None, 32)  
        lives_text = font.render(str(self.spaceship.get_lives()), True, (255, 255, 255)) 
        self.screen.blit(lives_text, (25, 20)) 
        
        font = pygame.font.Font(None, 32)  
        lives_text = font.render(str(self.enemyship.get_lives()), True, (255, 255, 255)) 
        self.screen.blit(lives_text, (1060, 20)) 

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
