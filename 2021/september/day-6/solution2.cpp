class Solution
{
public:
    char slowestKey(vector<int> &releaseTimes, string keysPressed)
    {

        int n = releaseTimes.size();
        vector<int> transformed;
        transformed.push_back(releaseTimes[0]);
        for (int i = 1; i < n; i++)
        {
            transformed.push_back(releaseTimes[i] - releaseTimes[i - 1]);
        }
        int maxs = INT_MIN;
        int maxsIndex = 0;
        int temp = 0;
        for (int i = 0; i < n; i++)
        {
            temp = maxsIndex;
            if (transformed[i] >= maxs)
            {

                if (transformed[i] == maxs)
                {
                    if (keysPressed[i] > keysPressed[maxsIndex])
                        maxsIndex = i;
                    else
                        maxsIndex = temp;
                }
                else
                {
                    maxsIndex = i;
                    maxs = transformed[i];
                }
            }
        }
        return keysPressed[maxsIndex];
    }
};