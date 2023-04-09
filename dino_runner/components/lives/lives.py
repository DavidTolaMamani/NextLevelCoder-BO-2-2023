
from pygame.sprite import Sprite
from dino_runner.utils.constants import (
    SMALL_HEART
)
import random
from pygame.sprite import Sprite
from dino_runner.utils.constants import SCREEN_WIDTH


class Lives(Sprite):
    def __init__(self, image):
        self.image = image
        self.type = type
        self.rect = self.image.get_rect()
        self.rect.x = SCREEN_WIDTH
        self.rect.y = random.randint(270, 330)

    def update(self, game_speed, obstacles):
        self.rect.x -= game_speed
        if self.rect.x  < 0:
            obstacles.pop()
    
    def draw(self, screen):
        screen.blit(self.image, self.rect)
        screen.blit(self.image,(30,630))
