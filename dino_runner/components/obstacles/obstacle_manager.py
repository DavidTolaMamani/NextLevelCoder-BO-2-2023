
from dino_runner.components.obstacles.cactus import Cactus
from dino_runner.components.obstacles.bird import Bird
from dino_runner.components.obstacles.goku import Goku
from dino_runner.utils.constants import SMALL_CACTUS, BIRD, LARGE_CACTUS, GOKU
import pygame
import random
class ObstacleManager:
    def __init__(self):
        self.obstacles = []

    def update(self, game):
        if len(self.obstacles) == 0:
            self.obstacle_options = random.choice([Cactus(SMALL_CACTUS), Bird(BIRD), Goku(GOKU)])
            self.obstacles.append(self.obstacle_options)      

        for obstacle in self.obstacles:
            obstacle.update(game.game_speed, self.obstacles)
            if game.player.rect.colliderect(obstacle.rect):
                pygame.time.delay(500)
                game.playing = False
                game.death_counts += 1
                break

    def draw(self, screen):
        for obstacle in self.obstacles:
            obstacle.draw(screen)

    def reset_obstacles(self):
        self.obstacles = []
