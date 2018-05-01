import pygame as pg
import math
class Character(pg.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pg.image.load("img/guy.png")
        self.rect = self.image.get_rect()
        self.armImage = pg.image.load("img/arm.png")
        self.type = 0
        self.hooks = []
        Character.x,Character.y = (300, 600)

    def getAngle(self, start, end):
        return -math.atan2(end[1] - start[1], end[0] - start[0]) * 180 / math.pi

    def addGrapple(self, x, y):
        if (len(self.hooks) >= 1):
            self.hooks = []
        self.hooks.append({"color": (0, 0, 0), "start": (Character.x, Character.y), "end": (x, y), "width": 10})

    def renderGrapple(self, screen):
        tempX, tempY = Character.x, Character.y
        for hook in self.hooks:
            print(hook)
            pg.draw.line(screen, hook['color'], hook['start'], hook['end'], hook['width'])



