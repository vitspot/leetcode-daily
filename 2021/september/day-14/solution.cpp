#include <bits/stdc++.h>
using namespace std;
class Solution {
public:
    string reverseOnlyLetters(string s) {  
    int start = 0, end = s.size() - 1;
        while (start < end) {
            while (start < end && !isalpha(s[start])) ++start; // Skipping non-alpha characters in the given character
            
            while (start < end && !isalpha(s[end])) --end; // Skipping non-alpha characters in the given character
            swap(s[start++], s[end--]); // swapping the alphabets only
        }
        return s;
        
    }
};