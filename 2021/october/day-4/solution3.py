class Solution:
        def islandPerimeter(self, grid: List[List[int]]) -> int:
            n = len(grid)
            m = len(grid[0])
            
            def dfs(x,y):
                if not (0<=x<n and 0<=y<m) or grid[x][y] == 0:
                    return 1
                if grid[x][y] == -1:
                    return 0
                grid[x][y] = -1
                paths = [(0,1),(0,-1),(1,0),(-1,0)]
                return sum(dfs(x+i,y+j) for i,j in paths)
            
            for r in range(n):
                for c in range(m):
                    if grid[r][c]: return dfs(r,c)