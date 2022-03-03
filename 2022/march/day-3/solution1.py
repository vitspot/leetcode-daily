```python
class Solution:
    def numberOfArithmeticSlices(self, nums: List[int]) -> int:
        N = len(nums)
        if N < 3: return 0
        cnt, prev_diff, total_slice = 0, inf, 0
        for i in range(N-1):
            diff = nums[i+1] - nums[i]
            if prev_diff != diff:
                prev_diff = diff
                cnt = 0
            else:
                cnt += 1
                total_slice += cnt
            print(prev_diff, diff, cnt, total_slice)
            
        return total_slice
```