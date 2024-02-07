import pygame as py



blockLayer = 1
playerLayer = 2

all_sprites = py.sprite.Group()
player_sprite = py.sprite.Group()


class Tile(py.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.tileSizeX, self.tileSizeY = 48, 48
        self.image = py.Surface((self.tileSizeX, self.tileSizeY))
        self.rect = self.image.get_rect()
        self.pos = py.math.Vector2(x * self.tileSizeX, y * self.tileSizeY)
    def draw(self, screen, offX):
        self.rect.topleft = (self.pos.x - offX, self.pos.y)
        screen.blit(self.image, self.rect)



