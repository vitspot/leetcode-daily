from collections import Counter
class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        check , text = Counter("balloon") , Counter(text)
        ans = inf
        for l,c in check.items(): # l->letter & c->count of that letter 
            ans = min(ans,text[l]//c)
        
        return ans
        