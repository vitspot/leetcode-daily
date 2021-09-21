# Written solution with explanation -> https://leetcode.com/explore/challenge/card/september-leetcoding-challenge-2021/638/week-3-september-15th-september-21st/3982/discuss/1476337/Python3-Clean-and-Simple-solution-or-Explained-in-detail

# One liner using groupby
class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        return max([0]+[len(list(g)) for k,g in groupby(nums) if k==1])

# Sliding Window
class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        ans = 0
        j = 0
        i = 0
        while(i<len(nums)):
            if nums[i] == 1:
                j = i+1
                while(j<len(nums) and nums[j]==1):
                    j+=1
                ans = max(ans,j-i)
                i = j
            else:
                i+=1
        return ans

