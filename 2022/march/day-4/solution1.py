class Solution:
          def champagneTower(self, poured: int, query_row: int, query_glass: int) -> float:
              dp = [poured]
          
              for i in range(1,query_row+1):
                  dp_new = [0] * (i+1)
                  for j in range(i):
                      prev = max((dp[j] - 1) / 2, 0)
                      dp_new[j] += prev
                      dp_new[j+1] += prev
                  dp = dp_new
                  
              return min(dp[query_glass],1)