import pygame as pg
class Level():
    def __init__(self):
        self.gravity = 5
        self.isGrounded = False

    def applyLevelPhysics(self, drawingSurface, sprite):
        self.applyGravity(sprite, self.isGrounded)
        self.ground(drawingSurface)
        self.detectGround(drawingSurface, sprite)

    def detectGround(self, drawingSurface,sprite):
        if(sprite.y >= drawingSurface.get_height() - 100):
            self.isGrounded = True
        else:
            self.isGrounded = False

    def ground(self, drawingSurface):
        pg.draw.line(drawingSurface, (0, 0, 255), (0, drawingSurface.get_height()), (drawingSurface.get_width(), drawingSurface.get_height()), 10)

    def applyGravity(self, sprite, isGrounded):
        if not isGrounded:
            sprite.y += self.gravity
