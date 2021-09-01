class Solution {
public:
    int arrayNesting(vector<int>& nums) {

        // maintain a list of visited indices
        vector<bool> visited(nums.size());
        int res = 0, count;
        
        // iteratote over the array while checking the maximum count
        for(int i=0; i<nums.size(); i++){
            count = 0;
            while(!visited[i]){
                count++;
                visited[i] = true;
                i = nums[i];
            }
            res = res>count? res: count;
        }
        return res;
    }
};