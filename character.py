import pygame as pg
import math
class Character(pg.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pg.image.load("img/guy.png")
        self.armImage = pg.image.load("img/arm.png")
        self.type = 0
        self.hooks = []
        self.tempX, self.tempY = 0, 0
        self.isGrappled = False
        Character.x,Character.y = (30, 300)
        self.height, self.width = self.image.get_height(), self.image.get_width()
        self.rect = {"x": Character.x, "y": Character.y, "width": self.image.get_height(), "height": self.image.get_width()}

    def getAngle(self, start, end):
        return -math.atan2(end[1] - start[1], end[0] - start[0]) * 180 / math.pi

    def addGrapple(self, x, y):
        self.tempX, self.tempY = Character.x, Character.y
        self.isGrappled = False
        if (len(self.hooks) >= 1):
            self.hooks = []
        self.hooks.append({"color": (0, 0, 0), "start": (Character.x, Character.y), "end": (x, y), "width": 1, "height":(20)})

    def renderGrapple(self, screen):
        for hook in self.hooks:
            if not self.isGrappled:
                self.tempX += (hook['end'][0] - Character.x) * .1
                self.tempY += (hook['end'][1] - Character.y) * .1
            pg.draw.line(screen, hook['color'], hook['start'], (self.tempX, self.tempY), hook['width'])

    def flyToGrapple(self, hook):
        Character.x += (hook['end'][0] - self.x) * .1
        Character.y += (hook['end'][1] - self.y) * .1

    def checkHookCollision(self, platform):
        rect1 = platform.rect
        for hook in self.hooks:
            if (rect1["x"] < self.tempX + hook["height"] and
               rect1["x"] + rect1["width"] > self.tempX and
               rect1["y"] < self.tempY + hook["height"] and
               rect1["height"] + rect1["y"] > self.tempY):
                self.isGrappled = True
                hook['isGrappled'] = True
                self.flyToGrapple(hook)

    def checkCollision(self, platform):
         rect1 = platform.rect
         if (rect1["x"] < self.rect["x"] + self.rect["height"] and
               rect1["x"] + rect1["width"] > self.rect["x"] and
               rect1["y"] < self.rect["y"] + self.rect["height"] and
               rect1["height"] + rect1["y"] > self.rect["y"]):
                print("collided")
