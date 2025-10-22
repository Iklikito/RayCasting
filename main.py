import pygame
import sys
import math
ROWS = 10
COLS = 15

TILESIZE = 32
WINDOWWIDTH = TILESIZE * COLS
WINDOWHEIGHT = TILESIZE * ROWS

FOV = 60 *(math.pi/180)
RESOLUTION = 4
NUMBEROFRAYS = WINDOWWIDTH/RESOLUTION
SCREEN = pygame.display.set_mode((WINDOWWIDTH, WINDOWHEIGHT))
while(True):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    SCREEN.fill((255,0,0))
    pygame.display.update()