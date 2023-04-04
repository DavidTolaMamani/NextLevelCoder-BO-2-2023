from dino_runner.components.obstacles.obstacle import Obstacle
from dino_runner.utils.constants import GOKU

class Goku(Obstacle):

    def __init__(self, image_list):
        super().__init__(image_list[0], animated=True)
        self.rect.y = 290
        self.flight_index = 0  

    def animate(self):
        super().animate()
        if self.flight_index < 5:
            self.image = GOKU[0]
        else:
            self.image = GOKU[1]
        self.flight_index = (self.flight_index + 1) 
        
        if self.flight_index >= 10:
            self.flight_index = 0