class Solution {
public:
    string shiftingLetters(string s, vector<int>& shifts) {
        int n = shifts.size();
        //calculating cummulative shift 
        //from the last given shift to first one.
        for(int i = n-2; i>=0; i--){
            shifts[i] = (shifts[i] + shifts[i+1]);
            //if cummulative shift adds upto > 26
            //we take modulo 26 since  shift uptil 26 revert to 
            //original character
            shifts[i] = shifts[i]%26;
        }
        for(int i = 0; i < n; i++) {
            //doing operations on absolute int value for convenience
            int c  = s[i] - 'a';
            //add the particular shifts
            c = c + shifts[i];
            //taking modulo 26 since the effective shifts
            //can only be upto 25
            c = c % 26;
            //adding 'a' to bring the integer into lowercase letters range
            c = c + 'a';
            //convert to char and store.
            s[i] = (char)c;
  
        }
        return s;
    }
};