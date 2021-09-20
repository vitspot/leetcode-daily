#   Longest Turbulent Subarray

Given an integer array arr, return the length of a maximum size turbulent subarray of arr.

A subarray is turbulent if the comparison sign flips between each adjacent pair of elements in the subarray.

More formally, a subarray [arr[i], arr[i + 1], ..., arr[j]] of arr is said to be turbulent if and only if:

For i <= k < j:
arr[k] > arr[k + 1] when k is odd, and
arr[k] < arr[k + 1] when k is even.
Or, for i <= k < j:
arr[k] > arr[k + 1] when k is even, and
arr[k] < arr[k + 1] when k is odd.


### Example 1:

        Input: arr = [9,4,2,10,7,8,8,1,9]

        Output: 5

        Explanation: arr[1] > arr[2] < arr[3] > arr[4] < arr[5]

### Example 2:

        Input: arr = [4,8,12,16]

        Output: 2

### Example 3:

        Input: arr = [100]

        Output: 1




**Reference**: https://leetcode.com/explore/challenge/card/september-leetcoding-challenge-2021/638/week-3-september-15th-september-21st/3976/

## Solutions
1. [Submission 1](./solution.cpp)

```cpp
        int maxTurbulenceSize(vector<int>& arr) {
         int result = 1, prevEle = 0; 
        int j = 0;
        for (int i = 1; i < arr.size(); ++i) {
            int differ = arr[i] - arr[i-1]; 
            if (differ == 0) j = i; 
            else if ((long)prevEle * differ > 0) j = i-1;
            
            result = max(result, i - j + 1); 
            prevEle = differ; 
        }
        return result; 
        
    }
```

