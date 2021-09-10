# Solution with explanation: https://leetcode.com/explore/challenge/card/september-leetcoding-challenge-2021/637/week-2-september-8th-september-14th/3970/discuss/1455765/Python-or-DP-or-With-detail-explanation

class Solution:
    def numberOfArithmeticSlices(self, nums: List[int]) -> int:
        N = len(nums)
        dp = [defaultdict(int) for _ in range(N)]
        
        ans = 0
        for i in range(1,N):
            for j in range(i):
                diff = nums[i]-nums[j]
                count = dp[j][diff]
                dp[i][diff] += count + 1
                ans += count
        
        return ans