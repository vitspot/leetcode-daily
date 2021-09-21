# Max Consecutive Ones

Given a binary array **nums**, return the *maximum* number of consecutive **1**'s in the *array*.


### Example 1

    Input: nums = [1,1,0,1,1,1]
    Output: 3
    Explanation: The first two digits or the last three digits are consecutive 1s. The maximum number of consecutive 1s is 3.

### Example 2

    Input: nums = [1,0,1,1,0,1]
    Output: 2

### Constraints

     1 <= nums.length <= 105
     nums[i] is either 0 or 1

    
## Python3 Solution with Explanation

The first approach is to use sliding window, we iterate over the nums and if we encounter a **1**, we start exapanding our window till we encouter a **0**. After we encounter a **0** we can start with a fresh window, and also we store the maximum answer along the way.

```
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
```
The second approach is to use the inbuilt **groupby** function in python. This will help us to group similar items together, so the result of it will be like **[0,0,1,1,1,0,0,0])** -> **{0:[0,0],1:[1,1,1],0:[0,0,0]}**. Here we only care about the maximum number of 1 . The groupby function also gives us a key for every group so it makes our life easier to filter the objects.

Here k-> Key and g-> Group
```
class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        return max([0]+[len(list(g)) for k,g in groupby(nums) if k==1])
```

Note: Here we are using max([0]+the list generated) because in some case like nums = [0,0,0]. The generated list would be null, so the max function would through exception. So we can handle that case by adding a single [0] because the ans in the case would be 0


