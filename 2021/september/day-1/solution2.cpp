class Solution
{
public:
    int arrayNesting(vector<int> &a)
    {
        if (a.size() == 0)
            return 0;
        int longest = 1;

        for (int i = 0; i < a.size(); i++)
        {
            // if already visited
            if (a[i] == -1)
                continue;

            // atleast of length 1
            int len = 1;

            // mark first node as visited
            int node = a[i];
            a[i] = -1;

            // while we encounter node again
            while (node != -1)
            {
                if (a[node] == -1)
                    break;
                else
                    node = a[node];

                // increment and save longest list
                len++;
                longest = max(longest, len);
            }
        }
        return longest;
    }
};