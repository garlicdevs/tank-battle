import pygame
from tankbattle.env.constants import GlobalConstants


class ExplosionSprite(pygame.sprite.Sprite):
    def __init__(self, size, abs_x, abs_y, speed, sprites_bg):
        super().__init__()
        self.size = size
        self.images = sprites_bg
        self.image = self.images[0]
        self.rect = self.image.get_rect()
        self.rect.x = abs_x
        self.rect.y = abs_y
        self.count = 0
        self.current_frame = 0
        self.speed = speed
        self.type = GlobalConstants.EXPLOSION_OBJECT

    def update(self):
        self.count = self.count + 1
        if self.count % self.speed == 0:
            self.image = self.images[self.current_frame]
            self.current_frame = self.current_frame + 1

    def done(self):
        if self.current_frame >= 3:
            return True
        else:
            return False