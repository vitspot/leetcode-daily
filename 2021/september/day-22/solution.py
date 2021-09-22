class Solution:
    def maxLength(self, arr: List[str]) -> int:
        def subseq(s,i):
            if i>=n:
                self.ans = max(self.ans,len(s))
                return
            
            subseq(s,i+1)
            new = s+arr[i]
            if len(new) == len(set(new)):
                subseq(new,i+1)
        
        n = len(arr)
        self.ans = 0
        subseq("",0)
        return self.ans