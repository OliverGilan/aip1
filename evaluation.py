import pygame

def evaluate(grid):
    n = len(grid[0])
    visited = [row[:] for row in grid]
    depth = [row[:] for row in grid]

    queue = [(0,0,0)]

    while queue:
        coord = queue.pop(0)
        x = coord[0]
        y = coord[1]
        d = coord[2]

        if visited[x][y] == -1:
            continue
        
        visited[x][y] = -1
        depth[x][y] = d

        jump = grid[x][y]

        if (x+jump <= n):
            queue.append((x+jump, y, d+1)
        if (x-jump >= 0):
            queue.append((x-jump, y, d+1))
        if (y+jump <= n):
            queue.append((x, y+jump, d+1))
        if (y-jump >= 0):
            queue.append((x, y-jump, d+1))
    
    reachable = True if visited[n-1][n-1] == -1 else False

    k = 0
    if reachable is False:
        for row in grid:
            for col in grid[row]:
                if visited[row][col] != -1:
                    k = k - 1

        return k
    else:
        





    