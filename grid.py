# author: Adam Romano

import pygame, random
import properties

class Grid:

    def generate_move(self, x, y):
        minimum = 1
        maximum = max([properties.N_VALUE-1-x, x, properties.N_VALUE-1-y, y])
        if x == properties.N_VALUE//2 and y == properties.N_VALUE//2:
            return random.randint(minimum, properties.N_VALUE//2)
        elif x == properties.N_VALUE-1 and y == properties.N_VALUE-1:
            return 0
        else:
            return random.randint(minimum, maximum)

    def __init__(self):
        self.grid_width = properties.WINDOW_WIDTH
        self.grid_height = properties.WINDOW_HEIGHT
        self.cells = []

        for x in range(properties.N_VALUE):
            row = []
            for y in range(properties.N_VALUE):
                row.append(self.generate_move(x,y))
            self.cells.append(row)
            row = []

def draw_grid():
    for x in range(0,properties.WINDOW_WIDTH, properties.CELL_WIDTH):
        for y in range(0,properties.WINDOW_HEIGHT, properties.CELL_HEIGHT):
            pygame.draw.rect(surface, properties.BLACK, (x,y,properties.CELL_WIDTH, properties.CELL_HEIGHT), 1)

def populate_grid(grid):
    for x in range(properties.N_VALUE):
        for y in range(properties.N_VALUE):
            val = grid.cells[x][y]
            text = font.render(str(val), False, properties.BLACK)
            text_width = text.get_width()
            text_height = text.get_height()
            surface.blit(text, (y*(properties.CELL_HEIGHT)+(properties.CELL_WIDTH-text_width)//2, x*(properties.CELL_WIDTH)+(properties.CELL_HEIGHT-text_height)//2))

if __name__ == '__main__':
    grid = Grid()
    print(grid.cells)
    pygame.init()
    surface = pygame.display.set_mode((properties.WINDOW_WIDTH, properties.WINDOW_HEIGHT))
    pygame.display.set_caption('grid')
    surface.fill(properties.WHITE)
    font = pygame.font.SysFont('arial', 40)
    draw_grid()
    populate_grid(grid)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
        pygame.display.update()









