class Solution
{
public:
    int ans(vector<int> &dp, int n)
    {
        if (n == 0)
            return 0;
        if (n == 1 || n == 2)
            return 1;

        if (dp[n] != -1)
            return dp[n];

        dp[n] = ans(dp, n - 1) + ans(dp, n - 2) + ans(dp, n - 3);

        return dp[n];
    }

    int tribonacci(int n)
    {
        vector<int> dp(n + 1, -1);
        return ans(dp, n);
    }
};