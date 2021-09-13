class Solution
{
public:
    int orderOfLargestPlusSign(int n, vector<vector<int>> &mines)
    {

        int matrix[n][n];

        for (int i = 0; i < n; i++)
        {
            for (int j = 0; j < n; j++)
            {
                matrix[i][j] = 1;
            }
        }

        for (auto it : mines)
        {
            matrix[it[0]][it[1]] = 0;
        }

        int left[n][n], top[n][n], right[n][n], bottom[n][n];

        //Initializing left array;

        for (int i = 0; i < n; i++)
        {
            int ContinousOne = 0;
            for (int j = 0; j < n; j++)
            {
                if (matrix[i][j] == 0)
                {
                    ContinousOne = 0;
                    left[i][j] = 0;
                }

                else
                {
                    ContinousOne++;
                    left[i][j] = ContinousOne;
                }
            }
        }

        //Initializing right array;

        for (int i = n - 1; i >= 0; i--)
        {
            int ContinousOne = 0;
            for (int j = n - 1; j >= 0; j--)
            {
                if (matrix[i][j] == 0)
                {
                    ContinousOne = 0;
                    right[i][j] = 0;
                }

                else
                {
                    ContinousOne++;
                    right[i][j] = ContinousOne;
                }
            }
        }

        //Initializing top array;

        for (int i = 0; i < n; i++)
        {
            int ContinousOne = 0;
            for (int j = 0; j < n; j++)
            {
                if (matrix[j][i] == 0)
                {
                    ContinousOne = 0;
                    top[j][i] = 0;
                }

                else
                {
                    ContinousOne++;
                    top[j][i] = ContinousOne;
                }
            }
        }

        //Initializing bottom array;

        for (int i = 0; i < n; i++)
        {
            int ContinousOne = 0;
            for (int j = n - 1; j >= 0; j--)
            {
                if (matrix[j][i] == 0)
                {
                    ContinousOne = 0;
                    bottom[j][i] = 0;
                }

                else
                {
                    ContinousOne++;
                    bottom[j][i] = ContinousOne;
                }
            }
        }

        int maxLen = INT_MIN;

        for (int i = 0; i < n; i++)
        {

            for (int j = 0; j < n; j++)
            {

                int len = min(min(left[i][j], right[i][j]), min(top[i][j], bottom[i][j]));

                if (maxLen < len)
                    maxLen = len;
            }
        }

        return maxLen;
    }
};