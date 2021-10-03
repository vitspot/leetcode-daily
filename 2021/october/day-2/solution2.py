class Solution:
        def calculateMinimumHP(self, dungeon: List[List[int]]) -> int:
            n = len(dungeon)
            m = len(dungeon[0])
            
            @lru_cache(None)
            def rec(i,j):
                if i>=n or j>=m:
                    return inf
                
                if (i,j) == (n-1,m-1):
                    ans = max(1,1-dungeon[i][j])
                    return ans
                
                ans = min(rec(i+1,j),rec(i,j+1))
                ans-=dungeon[i][j]
                
                return max(1,ans)
            
            return rec(0,0)