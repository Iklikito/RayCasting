import pygame

ROWS = 10
COLS = 15
TILESIZE = 32

class Map:
    def __init__(self, filename):
        self.grid = []
        with open(filename) as file:
            for i in range(ROWS):
                self.grid.append(list(file.readline().rstrip("\n")))

    def render(self, screen):
        print(self.grid)

        for i in range(ROWS):
            for j in range(COLS):
                tile_x, tile_y = j * TILESIZE, i * TILESIZE

                rgb_entry = 40 + 215 * int(self.grid[i][j])
                pygame.draw.rect(screen, (rgb_entry, rgb_entry, rgb_entry), (tile_x, tile_y, TILESIZE-1, TILESIZE-1))