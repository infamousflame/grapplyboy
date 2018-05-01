import pygame
import math
pygame.init()

width = 600
height = 800

screen = pygame.display.set_mode((width, height))

clock = pygame.time.Clock()

isRunning = True

img = pygame.image.load("yikers2.png")
mouseX = 0
mouseY = 0


def rotate(surface, angle, pivot, offset):
    """Rotate the surface around the pivot point.

    Args:
        surface (pygame.Surface): The surface that is to be rotated.
        angle (float): Rotate by this angle.
        pivot (tuple, list, pygame.math.Vector2): The pivot point.
        offset (pygame.math.Vector2): This vector is added to the pivot.
    """
    rotated_image = pygame.transform.rotozoom(surface, -angle, 1)  # Rotate the image.
    rotated_offset = offset.rotate(angle)  # Rotate the offset vector.
    # Add the offset vector to the center/pivot point to shift the rect.
    rect = rotated_image.get_rect(center=pivot+rotated_offset)
    return rotated_image, rect  # Return the rotated image and shifted rect.


# IMAGE = pygame.Surface((img.get_width()*2, img.get_height()*2), pygame.SRCALPHA)
IMAGE = pygame.Surface((img.get_width(), img.get_height()), pygame.SRCALPHA)

IMAGE.blit(img, (-10, 0))
pivot = [200, 250]
offset = pygame.math.Vector2(50, -10)



def getAngle(start, end):
    return math.atan2(end[1] - start[1], end[0] - start[0]) * 180 / math.pi

while isRunning:
  clock.tick(50)
  screen.fill((255, 255, 255))
  # Process events
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
        isRunning = False
  # Clear the screen

  if event.type == pygame.MOUSEMOTION:
    mouseX = event.pos[0]
    mouseY = event.pos[1]

  rotated_image, rect = rotate(IMAGE, getAngle((200, 300), (mouseX, mouseY)), pivot, offset)
  screen.blit(rotated_image, rect)  # Blit the rotated image.

  # Update the screen
  pygame.display.flip()
