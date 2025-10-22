import pygame
import sys
import math
from map import Map

BLACK = (0, 0, 0)
RED   = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE  = (0, 0, 255)
WHITE = (255, 255, 255)

ROWS = 10
COLS = 15

TILESIZE = 32
WINDOWWIDTH = TILESIZE * COLS
WINDOWHEIGHT = TILESIZE * ROWS

FOV = 60 *(math.pi/180)
RESOLUTION = 4
NUMBEROFRAYS = WINDOWWIDTH/RESOLUTION
screen = pygame.display.set_mode((WINDOWWIDTH, WINDOWHEIGHT))

map = Map("map.txt")

view_mode = 1

while(True):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_k:
                view_mode ^= 1
    
    screen.fill(BLACK)
    
    if view_mode == 0:
        pass #TODO
    else:
        map.render(screen)

    
    pygame.display.update()