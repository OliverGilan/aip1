# library imports
import random
import pygame

# global variables
N = int(input("What value of N would you like to use for this grid (5,7,9,11)??\n"))
CELL_SIZE = 50
WIDTH = CELL_SIZE*N
HEIGHT = CELL_SIZE*N


# colors that will be used in the GUI
WHITE = (255, 255, 255)
BLACK = (40, 40, 40)

# grid object that will be used to create GUI
class Grid:
    def __init__(self):
        self.rows = N
        self.cols = N
        self.cells = []

        # generate grid according to part 2 in the assignment details
        for r in range(self.rows):
            arr = []
            for c in range(self.cols):
                minimum_move = 1
                maximum_move = max(self.rows-1-r, r, self.cols-1-c, c)
                # if its the middle cell, bounds are (1, N//2)
                if r == self.rows//2 and c == self.cols//2:
                    arr.append(random.randint(minimum_move, N//2))
                #if its the last cell, value should be 0
                elif r == self.rows-1 and c == self.cols-1:
                    arr.append(0)
                else:
                    # generate random int in (min, max)
                    arr.append(random.randint(minimum_move, maximum_move))
            #add the array to cells
            self.cells.append(arr)
            arr = []

def draw_grid(grid, window):
    # calculate dimensions of the cell based off window width, height and N value
    cell_width = int(round(WIDTH / N))
    cell_height = int(round(HEIGHT / N))

    # draw the grid itself
    for x in range(0, WIDTH, cell_width):
        pygame.draw.line(window, WHITE, (x, 0), (x, HEIGHT))
    for y in range(0, HEIGHT, cell_height):
        pygame.draw.line(window, WHITE, (0, y), (WIDTH, y))

    #add the numbers
    font = pygame.font.SysFont('marvel', 40)
    for r in range(grid.rows):
        for c in range(grid.cols):
            move = grid.cells[r][c]
            text = font.render(str(move), False, WHITE)
            text_width = text.get_width()
            text_height = text.get_height()
            window.blit(text, (c*(CELL_SIZE)+(CELL_SIZE-text_width)//2, r*(CELL_SIZE)+(CELL_SIZE-text_height)//2))

def main():
    #initialize a pygame
    pygame.init()
    window = pygame.display.set_mode((WIDTH, HEIGHT))
    grid = Grid()

    #running loop
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        pygame.display.set_caption("AI Project 1 - Oliver Gilan and Adam Romano")
        window.fill(BLACK)
        draw_grid(grid, window)
        pygame.display.update()

if __name__ == '__main__':
    main()
