# author: Adam Romano

import pygame, random

N_VALUE = 11
WINDOW_WIDTH = 600
WINDOW_HEIGHT = 600
CELL_WIDTH = int(round(WINDOW_WIDTH / N_VALUE))
CELL_HEIGHT = int(round(WINDOW_HEIGHT / N_VALUE))
BLACK = (0,0,0)
WHITE = (255,255,255)

class Grid:

    def generate_move(self, x, y):
        minimum = 1
        maximum = max([N_VALUE-1-x, x, N_VALUE-1-y, y])
        if x == N_VALUE//2 and y == N_VALUE//2:
            return random.randint(minimum, N_VALUE//2)
        elif x == N_VALUE-1 and y == N_VALUE-1:
            return 0
        else:
            return random.randint(minimum, maximum)

    def __init__(self):
        self.grid_width = WINDOW_WIDTH
        self.grid_height = WINDOW_HEIGHT
        self.cells = []

        for x in range(N_VALUE):
            row = []
            for y in range(N_VALUE):
                row.append(self.generate_move(x,y))
            self.cells.append(row)
            row = []

if __name__ == '__main__':
    grid = Grid()

    pygame.init()
    surface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
    pygame.display.set_caption('grid')
    surface.fill(WHITE)
    font = pygame.font.SysFont('arial',10)

    for x in range(0,WINDOW_WIDTH, CELL_WIDTH):
        for y in range(0,WINDOW_HEIGHT, CELL_HEIGHT):
            pygame.draw.rect(surface, BLACK, (x,y,CELL_WIDTH, CELL_HEIGHT), 1)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
        pygame.display.update()









