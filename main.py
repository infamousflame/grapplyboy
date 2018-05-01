import pygame as pg
from character import Character
from keyhandler import keyhandler
from level import Level

pg.init()

width = 600
height = 800

screen = pg.display.set_mode((width, height))
clock = pg.time.Clock()
isRunning = True

mouseX = 0
mouseY = 0

level1 = Level()
level1.addPlatform(200, 300)
level1.addPlatform(400, 500)
icon = pg.image.load("img/icon.png")
pg.display.set_icon(icon)

character = Character()
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
            character.addGrapple(event.pos[0], event.pos[1])

    level1.applyLevelPhysics(screen, character)
    character.renderGrapple(screen)
    screen.blit(character.image, (Character.x, Character.y))
    screen.blit(pg.transform.rotate(character.armImage, character.getAngle((Character.x + character.width/2, Character.y + character.height/2),
                                                                           (mouseX, mouseY))), (Character.x + character.width/2, Character.y + character.height/2))

    # Update the screen
    pg.display.flip()

