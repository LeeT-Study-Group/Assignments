class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        def dfs(i,j):
            if grid[i][j] in ["2","0"]:
                return
            grid[i][j] = "2"
            moves = [
                (-1,0), # U
                (0,1), # R
                (1,0), # D
                (0,-1) # L
            ]
            for i_c,j_c in moves:
                if 0<= i+i_c <len(grid) and 0<=j + j_c < len(grid[0]):
                    dfs(i+i_c,j+j_c)
        count = 0   
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j]=="1":
                    count += 1
                    dfs(i,j)
        return count