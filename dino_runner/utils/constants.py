import pygame
import os

# Global Constants
TITLE = "Chrome Dino Runner"
SCREEN_HEIGHT = 600
SCREEN_WIDTH = 1100
FPS = 30
IMG_DIR = os.path.join(os.path.dirname(__file__), "..", "assets")


# Assets Constants
ICON = pygame.image.load(os.path.join(IMG_DIR, "DinoWallpaper.png"))

RUNNING = [
    pygame.image.load(os.path.join(IMG_DIR, "Dino/DinoRun1.png")),
    pygame.image.load(os.path.join(IMG_DIR, "Dino/DinoRun2.png")),
]

RUNNING_SHIELD = [
    pygame.image.load(os.path.join(IMG_DIR, "Dino/DinoRun1Shield.png")),
    pygame.image.load(os.path.join(IMG_DIR, "Dino/DinoRun2.png")),
]

RUNNING_HAMMER = [
    pygame.image.load(os.path.join(IMG_DIR, "Dino/DinoDuck1Hammer.png")),
    pygame.image.load(os.path.join(IMG_DIR, "Dino/DinoRun2.png")),
]

JUMPING = pygame.image.load(os.path.join(IMG_DIR, "Dino/DinoJump.png"))
JUMPING_SHIELD = pygame.image.load(os.path.join(IMG_DIR, "Dino/DinoJumpShield.png"))
JUMPING_HAMMER = pygame.image.load(os.path.join(IMG_DIR, "Dino/DinoJumpHammer.png"))

DUCKING = [
    pygame.image.load(os.path.join(IMG_DIR, "Dino/DinoDuck1.png")),
    pygame.image.load(os.path.join(IMG_DIR, "Dino/DinoDuck2.png")),
]

DUCKING_SHIELD = [
    pygame.image.load(os.path.join(IMG_DIR, "Dino/DinoDuck1Shield.png")),
    pygame.image.load(os.path.join(IMG_DIR, "Dino/DinoDuck2.png")),
]

DUCKING_HAMMER = [
    pygame.image.load(os.path.join(IMG_DIR, "Dino/DinoDuck1Hammer.png")),
    pygame.image.load(os.path.join(IMG_DIR, "Dino/DinoDuck2.png")),
]
RUNNING_FLASH_SHIELD = [
    pygame.image.load(os.path.join(IMG_DIR, "Dino/DinoRun1FlashShield.png")),
    pygame.image.load(os.path.join(IMG_DIR, "Dino/DinoRun2FlashShield.png")),
]
JUMPING_FLASH_SHIELD = pygame.image.load(os.path.join(IMG_DIR, "Dino/DinoJumpFlashShield.png"))
DUCKING_FLASH_SHIELD = [
    pygame.image.load(os.path.join(IMG_DIR, "Dino/DinoDuck1FlashShield.png")),
    pygame.image.load(os.path.join(IMG_DIR, "Dino/DinoDuck2FlashShield.png")),
]
RUNNING_FLASH = [
    pygame.image.load(os.path.join(IMG_DIR, "Dino/DinoRun1Flash.png")),
    pygame.image.load(os.path.join(IMG_DIR, "Dino/DinoRun2Flash.png")),
]
JUMPING_FLASH = pygame.image.load(os.path.join(IMG_DIR, "Dino/DinoJumpFlash.png"))
DUCKING_FLASH = [
    pygame.image.load(os.path.join(IMG_DIR, "Dino/DinoDuck1Flash.png")),
    pygame.image.load(os.path.join(IMG_DIR, "Dino/DinoDuck2Flash.png")),
]


SMALL_CACTUS = [
    pygame.image.load(os.path.join(IMG_DIR, "Cactus/SmallCactus1.png")),
    pygame.image.load(os.path.join(IMG_DIR, "Cactus/SmallCactus2.png")),
    pygame.image.load(os.path.join(IMG_DIR, "Cactus/SmallCactus3.png")),
]
LARGE_CACTUS = [
    pygame.image.load(os.path.join(IMG_DIR, "Cactus/LargeCactus1.png")),
    pygame.image.load(os.path.join(IMG_DIR, "Cactus/LargeCactus2.png")),
    pygame.image.load(os.path.join(IMG_DIR, "Cactus/LargeCactus3.png")),
]

BIRD = [
    pygame.image.load(os.path.join(IMG_DIR, "Bird/Bird1.png")),
    pygame.image.load(os.path.join(IMG_DIR, "Bird/Bird2.png")),
]
GOKU = [
     pygame.image.load(os.path.join(IMG_DIR, "Goku/Goku1.png")),
    pygame.image.load(os.path.join(IMG_DIR, "Goku/Goku2.png")),
]

CLOUD = [ pygame.image.load(os.path.join(IMG_DIR, 'Other/Cloud.png')),
         pygame.image.load(os.path.join(IMG_DIR, 'Other/Cloud1.png'))]

SHIELD = pygame.image.load(os.path.join(IMG_DIR, 'Other/shield.png'))
HAMMER = pygame.image.load(os.path.join(IMG_DIR, 'Other/hammer.png'))

BG = pygame.image.load(os.path.join(IMG_DIR, 'Other/Track.png'))

HEART = pygame.image.load(os.path.join(IMG_DIR, 'Other/SmallHeart.png'))

RESET = pygame.image.load(os.path.join(IMG_DIR, 'Other/Reset.png'))
GAME_OVER = pygame.image.load(os.path.join(IMG_DIR, 'Other/GameOver.png'))

BG2 = pygame.image.load(os.path.join(IMG_DIR, 'Other/1476.png'))
SMALL_HEART = pygame.image.load(os.path.join(IMG_DIR, 'Other/SmallHeart.png'))

DEFAULT_TYPE = "default"

SHIELD_TYPE = "shield"

FONT_STYLE = 'Comic Sans MS'

COLORS = {
        'Black':(0,0,0),
        'white': (255, 255, 255)
}

BACKGROUND_MUSIC= os.path.join(IMG_DIR, 'Music/background_music.mp3')
MENU_MUSIC = os.path.join(IMG_DIR, 'Music/menu_music.mp3')

BOTTOM = [pygame.image.load(os.path.join(IMG_DIR, 'Other/R2.png')),
          pygame.image.load(os.path.join(IMG_DIR, 'Other/R3.png')),
          
         pygame.image.load(os.path.join(IMG_DIR, 'Other/R_1.png'))
          ]

BIRD1 = [
    pygame.image.load(os.path.join(IMG_DIR, "Bird/bird1.1.png")),
    pygame.image.load(os.path.join(IMG_DIR, "Bird/bird1.2.png")),
]

