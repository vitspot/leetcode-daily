class Solution:
        def islandPerimeter(self, grid: List[List[int]]) -> int:
            n = len(grid)
            m = len(grid[0])
            ans = 0
            for r in range(n):
                for c in range(m):
                    if grid[r][c] == 0: continue
                    cur = 4
                    if c+1<m and grid[r][c+1] == 1: cur-=1
                    if r+1<n and grid[r+1][c] == 1: cur-=1
                    if c-1>-1 and grid[r][c-1] == 1: cur-=1                   
                    if r-1>-1 and grid[r-1][c] == 1: cur-=1
                    ans+=cur
            
            return ans