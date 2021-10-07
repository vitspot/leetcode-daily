class Solution {
    public:
        vector<int> findDuplicates(vector<int>& nums) {
            //we can't use map or set as they take more space
            // one idea is to sort and check adjacent elements ut in that case time
            // complexity will be O(nlogn)
            //now it's given that numbers in array ae less than equal to length of array and all are positive
            // the idea is to traverse the array and go at the position of the number encounterd and make them negative, if they are already negative store abs value of n in another array as it will be going to the same position 2nd time.
            
            vector<int> results;
            for(int n:nums){
               
                if(nums[abs(n)-1] > 0) nums[abs(n)-1] *=-1;
                else
                    results.push_back(abs(n));
                
            }
            return results;
            
        }
    };