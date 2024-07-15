from typing import List

class Solution:
    def matrixScore(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        
        for i in range(rows):
            if grid[i][0] == 0:
                for j in range(cols):
                    grid[i][j] ^= 1  
        
        for j in range(1, cols):
            onecount = sum(grid[i][j] == 1 for i in range(rows))
            if onecount < rows / 2:
                for i in range(rows):
                    grid[i][j] ^= 1  
        score = 0  
        for i in range(rows):
            rowval = int("".join(map(str, grid[i])), 2)
            score += rowval
        
        return score  
