import pygame
import random
import pygame.mixer
from dino_runner.utils.constants import (BG, 
                                         ICON, 
                                         SCREEN_HEIGHT,
                                           SCREEN_WIDTH, 
                                           TITLE, 
                                           FPS,CLOUD,
                                             COLORS, 
                                             RUNNING_FLASH, 
                                             RESET,
                                               GAME_OVER,
                                               BG2, 
                                               BOTTOM,
                                               BACKGROUND_MUSIC,
                                               MENU_MUSIC
                                            )
from dino_runner.components.dinosaur import Dinosaur
from dino_runner.components.obstacles.obstacle_manager import ObstacleManager
from dino_runner.components.text_utils import TextUtils
from dino_runner.components.powerups.power_up_manager import PowerUpManager
from dino_runner.components.lives.lives_manager import LivesManager
class Game:
    def __init__(self):
        pygame.init()
        pygame.display.set_caption(TITLE)
        pygame.display.set_icon(ICON)
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        self.clock = pygame.time.Clock()
        self.playing = False
        self.game_speed = 20
        self.x_pos_bg = 0
        self.y_pos_bg = 380
        self.x_pos_cloud = 0
        self.y_pos_cloud = 0 
        self.player = Dinosaur()
        self.obstacle_manager = ObstacleManager()
        self.text_utils = TextUtils()
        self.points = 0
        self.game_running = True 
        self.death_count = 0
        self.powerup_manager = PowerUpManager()
        self.lives_manager = LivesManager()
        self.lives_count = 1
 
    
    def execute(self):
        while self.game_running:
            pygame.mixer.music.load(MENU_MUSIC)  
            pygame.mixer.music.set_volume(0.1)
            pygame.mixer.music.play(-1)
            if not self.playing:
                self.show_menu()
                
    def run(self):
        # Game loop: events - update - draw
        self.obstacle_manager.reset_obstacles()
        self.powerup_manager.reset_power_ups(self.points)
        self.playing = True
        while self.playing:
            self.events()
            self.update()
            self.draw()
     
    def events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.playing = False

    def update(self):
        user_input = pygame.key.get_pressed()
        self.player.update(user_input)
        self.obstacle_manager.update(self)
        self.powerup_manager.update(self.points, self.game_speed, self.player)
        self.lives_manager.update(self)

    def draw(self):
        self.clock.tick(FPS)
        self.screen.fill((255, 255, 255))
        self.draw_back()
        self.draw_background()
        self.draw_cloud()
        self.player.draw(self.screen)
        self.obstacle_manager.draw(self.screen)
        self.powerup_manager.draw(self.screen)
        self.lives_manager.draw(self.screen)
        self.score()
      
        pygame.display.update()
     #   pygame.display.flip()

    def draw_background(self):
        image_width = BOTTOM[1].get_width()

        self.screen.blit(BOTTOM[1], (self.x_pos_bg, self.y_pos_bg))
        self.screen.blit(BOTTOM[1], (image_width + self.x_pos_bg, self.y_pos_bg))
        if self.x_pos_bg <= -image_width:
            self.screen.blit(BOTTOM[1], (image_width + self.x_pos_bg, self.y_pos_bg))
            self.x_pos_bg = 0
        self.x_pos_bg -= self.game_speed

    def draw_back(self):
        image_width = BOTTOM[1].get_width()

        self.screen.blit(BOTTOM[0], (self.x_pos_bg, 0))
        self.screen.blit(BOTTOM[0], (image_width + self.x_pos_bg, 0))
        if self.x_pos_bg <= -image_width:
            self.screen.blit(BOTTOM[0], (image_width + self.x_pos_bg, 0))
            self.x_pos_bg = 0
        self.x_pos_bg -= self.game_speed
    
    def draw_cloud(self):
        type_cloud = random.randint(0, 1)
        image_width = CLOUD[type_cloud].get_width()
        if self.x_pos_cloud + image_width < 0: 
            self.x_pos_cloud = SCREEN_WIDTH + random.randint(800, 900)
            self.y_pos_cloud = random.randint(30, 120)
        self.x_pos_cloud -= self.game_speed 
        self.screen.blit(CLOUD[type_cloud], (self.x_pos_cloud, self.y_pos_cloud))
        

    def score(self):
        self.points +=1
        text, text_rect = self.text_utils.get_score_element(self.points)
        self.screen.blit(text, text_rect)
        self.player.check_invincibility(self.screen, self.text_utils)

    def show_menu(self):
        self.game_running = True
        self.screen.fill(COLORS['white'])
        self.print_menu_elements()
        self.obstacle_manager.reset_obstacles()
        pygame.display.update()
        self.handle_key_event_on_menu()

    def print_menu_elements(self):
        half_screen_height = SCREEN_HEIGHT //2
        half_screen_width = SCREEN_WIDTH //2

        if self.death_count == 0:
            self.screen.blit(BG2,(0,0))
            text, text_rect = self.text_utils.get_centered_message('Press Any key to start')
            self.screen.blit(text, text_rect)
            pygame.mixer.music.load(BACKGROUND_MUSIC)
            pygame.mixer.music.set_volume(0.1)
            pygame.mixer.music.play(-1)

        elif self.death_count > 0:
            score, score_rect = self.text_utils.get_centered_message('Your Score: ' + str(self.points), height= half_screen_height +50)
            death, death_rect = self.text_utils.get_centered_message('Death count: ' + str(self.death_count), height= half_screen_height +100)
            self.screen.blit(BOTTOM[0],(0,0))
            self.screen.blit(RESET,(half_screen_width - 21, half_screen_height -50) )
            self.screen.blit(GAME_OVER,(360, 60))
            self.screen.blit(score, score_rect)
            self.screen.blit(death, death_rect)

        self.screen.blit(RUNNING_FLASH[0], (half_screen_width - 30, half_screen_height -160))
 
    def handle_key_event_on_menu(self):
       
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.game_running = False
                self.playing = False
                pygame.display.quit()
                pygame.quit()
                exit()
            if event.type == pygame.KEYDOWN:
                self.run()


       



        
