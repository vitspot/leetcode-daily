# My write up solution: (https://leetcode.com/problems/orderly-queue/discuss/1445861/python-3-clean-concise-solution-with-detail-explanation)
# siddheshwar day-5 python solution

  class Solution:
    def orderlyQueue(self, s: str, k: int) -> str:
        if k==1:
            best = s
            for i in range(len(s)):
                cur = s[i:]+s[:i] 
                if cur<best : best = cur
            return best
                        
        return "".join(sorted(s))

# One liner
class Solution:
    def orderlyQueue(self, s: str, k: int) -> str:
            return min(s[i:]+s[:i] for i in range(len(s))) if k==1 else "".join(sorted(s))
