# This is similar to the fibonacci series DP implementation, but rather than considering the last two, we here consider the last three.

class Solution:
    def tribonacci(self, n: int) -> int:
        dp = [0,1,1]
        for i in range(3,n+1):
            cur = dp[-1]+dp[-2]+dp[-3]
            dp.append(cur)
        return dp[n]

# This results in O(n) Time and space
# We can optimise it to O(n) Time and O(1) space by just keeping track of last three numbers

class Solution:
    def tribonacci(self, n: int) -> int:
    	a, b, c = 0, 1, 1
    	for i in range(n): a, b, c = b, c, a + b + c
    	return a