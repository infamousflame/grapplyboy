import pygame as pg
from character import Character
from level import Level

pg.init()

level1 = Level()
level1.addPlatform(200, 300)
level1.addPlatform(400, 500)
level1.addPlatform(400, 100)

icon = pg.image.load("img/icon.png")
pg.display.set_icon(icon)

character = Character()

level1.levelLoop(character)
