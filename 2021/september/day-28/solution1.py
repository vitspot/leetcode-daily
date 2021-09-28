class Solution:
    def sortArrayByParityII(self, nums: List[int]) -> List[int]:
        N = len(nums)
        i,j = 0,1
        while i<N and j<N:
            if nums[i]%2==0:
                i+=2
            elif nums[j]%2!=0:
                j+=2
            else:
                nums[i],nums[j] = nums[j],nums[i]
                i+=2
                j+=2
        
        return nums