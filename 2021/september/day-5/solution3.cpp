class Solution {
public:
    string orderlyQueue(string s, int k) {
        
        // If k is greater than 1, we can just return
        // the string sorted lexicographically
        if(k > 1){
            sort(s.begin(), s.end());
        }
        
        // Else we must return the minimum of all the
        // rotations of the string
        string res = s;
        int len = s.length();
        s += s;
        for(int i=0; i<len; i++){
            if(s.substr(i, len) < res)
                res = s.substr(i, len);
        }
        return res;
    }
};