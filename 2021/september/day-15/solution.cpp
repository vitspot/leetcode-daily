#include <bits/stdc++.h>
using namespace std;
class Solution
{
public:
    int maxTurbulenceSize(vector<int> &arr)
    {
        int result = 1, prevEle = 0;
        int j = 0;
        for (int i = 1; i < arr.size(); ++i)
        {
            int differ = arr[i] - arr[i - 1];
            if (differ == 0)
                j = i;
            else if ((long)prevEle * differ > 0)
                j = i - 1;

            result = max(result, i - j + 1);
            prevEle = differ;
        }
        return result;
    }
};