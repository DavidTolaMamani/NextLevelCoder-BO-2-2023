import pygame

from dino_runner.utils.constants import FONT_STYLE, COLORS, SCREEN_HEIGHT, SCREEN_WIDTH,BACKGROUND_MUSIC

class TextUtils:
   
    def get_score_element(self, points):
        font = pygame.font.SysFont(FONT_STYLE, 33)
        text = font.render('Points: ' + str(points), True, COLORS['white'])
        text_rect = text.get_rect()
        text_rect.center = (1000,50) 
        return text,text_rect
    
    def get_centered_message(self, message, width = SCREEN_WIDTH // 2, height = SCREEN_HEIGHT // 2):
        font = pygame.font.SysFont(FONT_STYLE, 30)
        text = font.render(str(message), True, COLORS['Black'])
        text_rect = text.get_rect()
        text_rect.center = (width, height)
        return text,text_rect

    def show_shield_time(self, screen,time_to_show):
                font = pygame.font.SysFont(FONT_STYLE, 30)
                text = font.render("Shield: " + str(time_to_show) + "s", True, ('white'))
                screen.blit(text, (10, 10))

        
