class Solution
{
public:
    string orderlyQueue(string s, int k)
    {
        if (k == 1)
        {
            string result = s;
            for (int i = 0; i < s.length(); i++)
            {
                result = min(result, s.substr(i) + s.substr(0, i));
                // rotating the string one by one and finding minimum
                //taking first letter and appending at last
            }
            return result;
        }
        sort(s.begin(), s.end());
        return s;
    }
};