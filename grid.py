# library imports
import random
import time
from termcolor import colored


# global variables
N = int(input("What value of N would you like to use for this grid (5,7,9,11)??\n"))

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

def print_grid(position,grid, visited):
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if i == position[0] and j == position[1]:
                print(colored("{:2.0f}".format(grid[i][j]), 'red'), end=" ")
                visited.append((i,j))
            elif (i,j) in visited:
                print(colored("{:2.0f}".format(grid[i][j]), 'blue'), end=" ")
            else:
                print("{:2.0f}".format(grid[i][j]), end=" ")
        print()

def run_loop(grid, visited=[]):
    # path = [(0, 0), (1, 0), (1, 1), (0, 1), (0, 2), (1, 2), (2, 2)]
    for tup in path:
        print_grid(tup, grid, visited)
        time.sleep(1)
        print('=========')

if __name__ == '__main__':
    grid = Grid()
    run_loop(grid.cells)
