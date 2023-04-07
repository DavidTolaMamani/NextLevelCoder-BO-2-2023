from dino_runner.components.lives.heart import Heart
from dino_runner.utils.constants import SMALL_HEART

import pygame

from dino_runner.components.lives.heart import Heart 

class LivesManager:
    def __init__(self):
        self.obstacles = []

    def update(self, game):
        if len(self.obstacles) == 0:
            self.obstacles.append(Heart(SMALL_HEART))      

        for obstacle in self.obstacles:
            obstacle.update(game.game_speed, self.obstacles)
            if game.player.rect.colliderect(obstacle.rect):
                print("entro al metodo")
                game.lives_count += 1
                print("suma vidas",game.lives_count)
                self.obstacles.remove(obstacle)         

    def draw(self, screen):
        for obstacle in self.obstacles:
            obstacle.draw(screen)

    def reset_obstacles(self):
        self.obstacles = []
