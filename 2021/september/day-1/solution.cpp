class Solution {
public:
    int arrayNesting(vector<int>& nums) {
        vector<bool> visited(nums.size());
        int res = 0, count;
        
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