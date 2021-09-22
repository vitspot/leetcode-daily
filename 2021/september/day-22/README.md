#   Maximum Length of a Concatenated String with Unique Characters
Given an array of strings arr. String s is a concatenation of a sub-sequence of arr which have unique characters.

Return the maximum possible length of s.

## Example 1:

Input: arr = ["un","iq","ue"]
Output: 4
Explanation: All possible concatenations are "","un","iq","ue","uniq" and "ique".
Maximum length is 4.

## Example 2:

Input: arr = ["cha","r","act","ers"]
Output: 6
Explanation: Possible solutions are "chaers" and "acters".

## Example 3:

Input: arr = ["abcdefghijklmnopqrstuvwxyz"]
Output: 26

## Constraints:

> 1 <= arr.length <= 16
> 1 <= arr[i].length <= 26
> arr[i] contains only lower case English letters.

## Solution Approach: 

> The brute force idea of the problem is to find all possible subsequence and consider only subsequences which doesn't have a duplicate character.

> A slight optimisation will majorly bring down our time complexity. Instead of generating all possible subsequence, we can check if it will be a valid path before hand. Seeing the code will make it more clear.