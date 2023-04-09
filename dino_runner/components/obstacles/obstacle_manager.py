from dino_runner.components.obstacles.cactus import Cactus
from dino_runner.components.obstacles.bird import Bird
from dino_runner.components.obstacles.goku import Goku
from dino_runner.components.obstacles.bird1 import Bird1
from dino_runner.utils.constants import SMALL_CACTUS, BIRD, LARGE_CACTUS, GOKU, BIRD1
import pygame
import random

class ObstacleManager:
    def __init__(self):
        self.obstacles = []

    def update(self, game):
        if len(self.obstacles) == 0 :
            self.obstacle_options = random.choice([Cactus(SMALL_CACTUS), Bird(BIRD), Goku(GOKU), Cactus(LARGE_CACTUS), Bird1(BIRD1)])
            self.obstacles.append(self.obstacle_options)          
        
        for obstacle in self.obstacles:
            if game.points == 900 or game.points ==3600:
                game.game_speed +=3
            obstacle.update(game.game_speed, self.obstacles)
            if game.player.rect.colliderect(obstacle.rect):
                if not game.player.shield:
                    if game.lives_count > 1:
                        self.obstacles.remove(obstacle)
                    if game.lives_count >= 1:
                        game.lives_count -= 1
                        print("rest", game.lives_count)
                    if game.lives_count < 1:
                        pygame.time.delay(500)
                        game.playing = False
                        game.death_count += 1
                        break

    def draw(self, screen):
        for obstacle in self.obstacles:
            obstacle.draw(screen)

    def reset_obstacles(self):
        self.obstacles = []
