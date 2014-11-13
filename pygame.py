import pygame, sys
from pygame.locals import *

# color ===========================================================
# color
pygame.Color(255, 0, 0)
myColor = pygame.Color(255, 0, 0, 128)
myColor == (255, 0, 0, 128)

# rect
spamRect = pygame.Rect(10, 20, 200, 300)
spamRect == (10, 20, 200, 300)
spamRect.right == 210

# pic
catImg = pygame.image.load('cat.png')
DISPLAYSURF.fill(WHITE)
DISPLAYSURF.blit(catImg, (catx, caty))
pygame.display.update()
fpsClock.tick(FPS)

# color ===========================================================
