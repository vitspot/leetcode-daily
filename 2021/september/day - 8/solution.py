class Solution:
    def shiftingLetters(self, s: str, shifts: List[int]) -> str:
        s , running_sum = list(s) , 0
        
        for i in range(len(shifts)-1,-1,-1):
            running_sum += shifts[i]
            
            # This is to make sure we dont go out of bounce in alphabets and choose some other character
            s[i] = chr(((ord(s[i]) - ord('a') + running_sum) % 26) + ord('a'))
        
        return ''.join(s)
                
                
            
            
        