class Solution:
        def calculateMinimumHP(self, dungeon: List[List[int]]) -> int:
            n = len(dungeon)-1
            m = len(dungeon[0])-1
            
            dp = dungeon
            dp[n][m] = max(1,1-dp[n][m])
            
            for r in reversed(range(n)):
                dp[r][m] = max(1,dp[r+1][m]-dp[r][m])
            
            for c in reversed(range(m)):
                dp[n][c] = max(1,dp[n][c+1]-dp[n][c])
            
            for r in reversed(range(n)):
                for c in reversed(range(m)):
                    ans = min(dp[r+1][c],dp[r][c+1])-dp[r][c]
                    dp[r][c] = max(1,ans)
            
            return dp[0][0]