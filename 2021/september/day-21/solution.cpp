#include <bits/stdc++.h>
using namespace std;

class Solution
{
public:
    int findMaxConsecutiveOnes(vector<int> &nums)
    {

        int n = nums.size();
        int maxCount = INT_MIN;
        int count = 0;
        for (int i = 0; i < n; i++)
        {
            if (nums[i])
                count++;
            else
                count = 0;
            if (count > maxCount)
            {
                maxCount = count;
            }
        }
        return maxCount;
    }
};