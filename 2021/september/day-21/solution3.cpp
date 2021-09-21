class Solution {
public:
    int findMaxConsecutiveOnes(vector<int>& nums) {
        int curr = 0;
        int count = 0;
        for(int i=0; i<nums.size(); i++){
            if(nums[i] == 1){
                count++;
                cout << count << " ";
            } else{
                if(count > curr){
                    curr =  count;
                }
                count = 0;
            }
        }
        if(count > curr){
            curr =  count;
        }
        
        return curr;
    }
};