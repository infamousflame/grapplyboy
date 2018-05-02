import pygame as pg
from platform import Platform
from character import Character

class Level():
    def __init__(self):
        self.gravity = 10
        self.isGrounded = False
        self.platforms = []

    def applyLevelPhysics(self, drawingSurface, sprite):
        self.applyGravity(sprite, self.isGrounded)
        self.ground(drawingSurface)
        self.detectGround(drawingSurface, sprite)
        self.drawPlatforms(self.platforms, drawingSurface)
        self.collisions(self.platforms, sprite)
    def detectGround(self, drawingSurface,sprite):

        if(Character.y >= drawingSurface.get_height() - 100):
            self.isGrounded = True
        elif(sprite.isGrappled):
            self.isGrounded = True

        if(Character.y <= drawingSurface.get_height() - 100):
            self.isGrounded = False


    def ground(self, drawingSurface):
        pg.draw.line(drawingSurface, (0, 0, 255), (0, drawingSurface.get_height()), (drawingSurface.get_width(), drawingSurface.get_height()), 10)

    def addPlatform(self, x, y):
        self.platforms.append(Platform(x, y))

    def drawPlatforms(self, platforms, screen):
        for platform in platforms:
            platform.drawPlatForm(platform.x, platform.y, screen)

    def applyGravity(self, sprite, isGrounded):
        if not isGrounded:
            Character.y += self.gravity

    def collisions(self, platforms, character):
        self.checkHookCollision(platforms, character)
        self.checkCollision(platforms, character)

    def checkHookCollision(self, platforms, character):
        for platform in platforms:
            character.checkHookCollision(platform)

    def checkCollision(self, platforms, character):
        for platform in platforms:
            character.checkCollision(platform)
