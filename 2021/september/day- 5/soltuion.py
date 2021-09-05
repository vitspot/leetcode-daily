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