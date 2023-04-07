import random
from dino_runner.components.lives.lives import Lives
from dino_runner.utils.constants import SCREEN_WIDTH


class Heart(Lives):
    def __init__(self, image):
        super().__init__(image)
        