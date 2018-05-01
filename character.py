import pygame as pg
import math
class Character(pg.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pg.image.load("img/guy.png")
        self.armImage = pg.image.load("img/arm3.png")
        self.type = 0
        self.x,self.y = (300, 100)

    def getAngle(self, start, end):
        return -math.atan2(end[1] - start[1], end[0] - start[0]) * 180 / math.pi

