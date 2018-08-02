import pygame
from tankbattle.env.constants import GlobalConstants


class WallSprite(pygame.sprite.Sprite):
    def __init__(self, size, pos_x, pos_y, sprite_bg):
        super().__init__()
        self.size = size
        self.pos_x = pos_x
        self.pos_y = pos_y
        self.type = GlobalConstants.HARD_OBJECT
        self.image = sprite_bg
        self.rect = self.image.get_rect()
        self.rect.x = pos_x * self.size
        self.rect.y = pos_y * self.size