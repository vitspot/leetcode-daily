#   Reverse Only Letters

Given a string s, reverse the string according to the following rules:

All the characters that are not English letters remain in the same position.
All the English letters (lowercase or uppercase) should be reversed.
Return s after reversing it.


### Example 1:

        Input: s = "ab-cd"
        
        Output: "dc-ba"

### Example 2:

        Input: s = "a-bC-dEf-ghIj"

        Output: "j-Ih-gfE-dCba"

### Example 3:

        Input: s = "Test1ng-Leet=code-Q!"

        Output: "Qedo1ct-eeLg=ntse-T!"




**Reference**: https://leetcode.com/explore/challenge/card/september-leetcoding-challenge-2021/637/week-2-september-8th-september-14th/3974/

## Solutions
1. [Submission 1](./solution.cpp)

```cpp
        string reverseOnlyLetters(string s) {  
            int start = 0, end = s.size() - 1;
                while (start < end) {
                    while (start < end && !isalpha(s[start])) ++start; // Skipping non-alpha characters in the given character
                    
                    while (start < end && !isalpha(s[end])) --end; // Skipping non-alpha characters in the given character
                    swap(s[start++], s[end--]); // swapping the alphabets only
                }
                return s;  
            }
```

