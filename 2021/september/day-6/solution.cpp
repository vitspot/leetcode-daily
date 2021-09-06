class Solution {
public:
    char slowestKey(vector<int>& releaseTimes, string keysPressed) {
        vector<int> a(26,-1);
        a[keysPressed[0]-97]=releaseTimes[0];
        int m=INT_MIN,idx;
        for(int i=1;i<keysPressed.size();i++)
        {
            a[keysPressed[i]-97] = max(a[keysPressed[i]-97],(releaseTimes[i]-releaseTimes[i-1]));
        }
        for(int i=0;i<26;i++)
        {
            cout<<a[i]<<" ";
            if(a[i]>=m)
            {
                m=a[i];
                idx=i;
            }
        }
        return idx+97;
        
    }
};
