class Solution
{
public:
    int maxNumberOfBalloons(string text)
    {

        map<char, int> mp;
        int sumOfFrequencies = 0;
        map<char, int>::iterator itr;
        int len = text.length();

        // finding the frequency
        for (int i = 0; i < len; i++)
        {
            if (text[i] == 'b' || text[i] == 'a' || text[i] == 'l' || text[i] == 'o' || text[i] == 'n')
                mp[text[i]]++;
        }
        // sum of all frequencies of characters
        for (itr = mp.begin(); itr != mp.end(); itr++)
        {

            sumOfFrequencies += itr->second;
        }
        if (mp.size() != 5 || sumOfFrequencies < 7)
            return 0;

        // finding minimum unit of string "balloon" to return
        int minUnit = INT_MAX;
        for (itr = mp.begin(); itr != mp.end(); itr++)
        {
            if (itr->first == 'l' || itr->first == 'o')
            {
                itr->second /= 2; // dividing by 2 so that we count ll or oo as 1 single unit
            }
            // finally finding minimum of all such units
            if (itr->second <= minUnit)
            {
                minUnit = itr->second;
            }
        }
        return minUnit;
    }
};