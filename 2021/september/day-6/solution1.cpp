class Solution
{
public:
    char slowestKey(vector<int> &releaseTimes, string keysPressed)
    {

        int max = releaseTimes[0];
        char letter = keysPressed[0];

        for (int i = 1; i < keysPressed.length(); i++)
        {
            if (max < releaseTimes[i] - releaseTimes[i - 1])
            {
                max = releaseTimes[i] - releaseTimes[i - 1];
                letter = keysPressed[i];
            }
            else if (max == releaseTimes[i] - releaseTimes[i - 1])
            {
                if (keysPressed[i] > keysPressed[i - 1])
                    letter = keysPressed[i];
            }
            else
                continue;
        }

        return letter;
    }
};