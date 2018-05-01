import pygame as pg
class Platform(pg.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pg.image.load('img/platform.png')
        self.x = x
        self.y = y
        self.rect = {"x": self.x, "y": self.y, "width": self.image.get_width(), "height": self.image.get_height()}

    def drawPlatForm(self, x, y, screen):
        screen.blit(self.image, (x, y))


