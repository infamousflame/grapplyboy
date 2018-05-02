import pygame as pg
from platform import Platform
from character import Character
from keyhandler import keyhandler

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

    def levelLoop(self, character):
        width = 600
        height = 800
        clock = pg.time.Clock()
        screen = pg.display.set_mode((width, height))
        isRunning = True
        mouseX = 0
        mouseY = 0
        while isRunning:
            clock.tick(50)
            screen.fill((255, 255, 255))
            # Process events
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    isRunning = False
            # Clear the screen
                if event.type == pg.KEYDOWN:
                    keyhandler(event.key, True)
                elif event.type == pg.KEYUP:
                    keyhandler(event.key, False)

                if event.type == pg.MOUSEMOTION:
                    mouseX = event.pos[0]
                    mouseY = event.pos[1]


                if event.type == pg.MOUSEBUTTONDOWN:
                    if event.button == 1:
                        character.addGrapple(event.pos[0], event.pos[1])
                elif event.type == pg.MOUSEBUTTONUP:
                    if event.button == 3:
                        character.removeGrapple()

            self.applyLevelPhysics(screen, character)
            character.renderGrapple(screen)
            character.applyMomentum()
            screen.blit(character.image, (Character.x, Character.y))
            screen.blit(pg.transform.rotate(character.armImage, character.getAngle((Character.x + character.width/2, Character.y + character.height/2),
                                                                                   (mouseX, mouseY))), (Character.x + character.width/2, Character.y + character.height/2))

            # Update the screen
            pg.display.flip()

