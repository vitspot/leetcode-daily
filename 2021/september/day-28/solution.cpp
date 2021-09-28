// two pointers approach to solve easy approach
// take two pointers one check the even positions and one checks for odd position
// traverse and if odd/even mismatches swap
class Solution
{
public:
    vector<int> sortArrayByParityII(vector<int> &nums)
    {
        int ipointer = 0, jpointer = 1;
        while (ipointer < nums.size() && jpointer < nums.size())
        {

            if (nums[ipointer] % 2 == 0)
                ipointer += 2;

            else if (nums[jpointer] % 2 == 1)
                jpointer += 2;

            else
                (swap(nums[ipointer], nums[jpointer]));
        }

        return nums;
    }
};