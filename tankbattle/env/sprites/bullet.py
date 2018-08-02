import pygame
from tankbattle.env.constants import GlobalConstants


class BulletSprite(pygame.sprite.Sprite):
    def __init__(self, size, tile_size, direction, speed, pos_x, pos_y, owner, sprite_bg):
        super().__init__()

        self.size = size
        self.tile_size = tile_size
        self.direction = direction
        self.speed = speed
        self.pos_x = pos_x
        self.pos_y = pos_y
        self.type = GlobalConstants.BULLET_OBJECT
        self.owner = owner
        self.image = sprite_bg

        self.rect = self.image.get_rect()
        adj_pos_x = 0
        adj_pos_y = 0
        if direction == GlobalConstants.LEFT_ACTION:
            adj_pos_x = -self.tile_size/2
        elif direction == GlobalConstants.RIGHT_ACTION:
            adj_pos_x = self.tile_size/2
        elif direction == GlobalConstants.UP_ACTION:
            adj_pos_y = -self.tile_size/2
        elif direction == GlobalConstants.DOWN_ACTION:
            adj_pos_y = self.tile_size/2
        self.rect.x = pos_x * self.tile_size + self.tile_size/2 - int(self.size/2) + adj_pos_x
        self.rect.y = pos_y * self.tile_size + self.tile_size/2 - int(self.size/2) + adj_pos_y

    def update(self):
        if self.direction == GlobalConstants.LEFT_ACTION:
            self.rect.x = self.rect.x - self.speed
        elif self.direction == GlobalConstants.RIGHT_ACTION:
            self.rect.x = self.rect.x + self.speed
        elif self.direction == GlobalConstants.UP_ACTION:
            self.rect.y = self.rect.y - self.speed
        elif self.direction == GlobalConstants.DOWN_ACTION:
            self.rect.y = self.rect.y + self.speed
