import pygame as pg
import math
from character import Character
pg.init()

width = 600
height = 800

screen = pg.display.set_mode((width, height))

clock = pg.time.Clock()

isRunning = True

mouseX = 0
mouseY = 0

character = Character()

while isRunning:

    clock.tick(50)
    screen.fill((255, 255, 255))
    # Process events
    for event in pg.event.get():
        if event.type == pg.QUIT:
            isRunning = False
    # Clear the screen

    if event.type == pg.MOUSEMOTION:
        mouseX = event.pos[0]
        mouseY = event.pos[1]

    screen.blit(character.image, (character.x, character.y))
    screen.blit(pg.transform.rotate(character.armImage, character.getAngle((character.x + character.rect.width/2, character.y + character.rect.height/2), (mouseX, mouseY))), (character.x + character.rect.width/2, character.y + character.rect.height/2))

    # Update the screen
    pg.display.flip()
