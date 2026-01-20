from typing import List
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        li = []
        r = len(grid)
        c = len(grid[0])
        for i in range(r):
            for j in range(c):
                if grid[i][j] == 2:
                    li.append([i, j, 0])
        minutes = 0
        while(len(li) > 0):
            x,y, level = li.pop(0)
            if (x > 0 and grid[x - 1][y] == 1):
                grid[x - 1][y] = 2
                li.append([x - 1, y, level + 1])

            if (x < r - 1 and grid[x + 1][y] == 1):
                grid[x + 1][y] = 2
                li.append([x+1, y, level + 1])
            
            if (y > 0 and grid[x][y - 1] == 1):
                grid[x][y - 1] = 2
                li.append([x, y - 1, level + 1])

            if (y < c - 1 and grid[x][y + 1] == 1):
                grid[x][y + 1] = 2
                li.append([x, y + 1, level + 1])
            minutes = max(level, minutes)
        for i in range(r):
            for j in range(c):
                if grid[i][j] == 1:
                    return -1
                    
        return minutes