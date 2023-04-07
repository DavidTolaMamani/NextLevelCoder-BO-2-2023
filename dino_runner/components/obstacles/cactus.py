import random
from dino_runner.components.obstacles.obstacle import Obstacle
from dino_runner.utils.constants import SMALL_CACTUS, LARGE_CACTUS

class Cactus(Obstacle):
    def __init__(self, image_list):
        self.type = random.randint(0, 2)
        if image_list == SMALL_CACTUS:
            super().__init__(image_list[self.type])
            self.rect.y = 325
        elif image_list == LARGE_CACTUS:
            super().__init__(image_list[self.type])
            self.rect.y = 300
    
