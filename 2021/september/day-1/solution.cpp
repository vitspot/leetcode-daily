class Solution {
public:
    int arrayNesting(vector<int>& nums) {
        int answer =0;
        for(int i=0; i<nums.size();i++){
            int takeCount = 0;
            int newi = i;
            while(nums[newi] !=-1){ 
                // traversing acc. to question
                int oldi = newi;
                newi = nums[newi];
                nums[oldi]=-1;
                takeCount++;
                
            }
            answer = max(answer, takeCount);
        }
        return answer;
        
    }
};
