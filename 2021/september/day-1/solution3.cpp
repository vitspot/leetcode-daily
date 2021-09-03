class Solution
{
public:
    int arrayNesting(vector<int> &nums)
    {

        int n = nums.size();
        vector<int> visited(n, 0);
        int count = 0;
        int maxcount = 0;
        for (int i = 0; i < n; i++)
        {

            // if the element is not visited then we proceed with the logic 

            if (!visited[i])
            {
                count = 0;
                int curr = nums[i];

                // looping through the elements till we encounter duplicate

                while (curr != i)
                {
                    visited[curr] = 1;
                    curr = nums[curr];
                    count++;
                }
            }

            maxcount = max(count, maxcount);
        }
        return maxcount + 1;
    }
};