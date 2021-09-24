# N-th Tribonacci Number

The Tribonacci sequence Tn is defined as follows:

T0 = 0, T1 = 1, T2 = 1, and Tn+3 = Tn + Tn+1 + Tn+2 for n >= 0.

Given n, return the value of Tn.

## Example 1:

    Input: n = 4
    Output: 4
    Explanation:
    T_3 = 0 + 1 + 1 = 2
    T_4 = 1 + 1 + 2 = 4

## Example 2:

    Input: n = 25
    Output: 1389537

## Constraints:

    0 <= n <= 37
    The answer is guaranteed to fit within a 32-bit integer, ie. answer <= 2^31 - 1.

## Solution Approach:

- First we initialize a DP vector with -1.
- Then we recursively call the function with n-1,n-2 and n-3 value.
- We use the DP vector to avoid calculating the same subproblems, we store the results in the vector and in each recursive call we check whether the answer has already been calculated for that particular n or not.
- If yes then we return the value from the vector, if not then we again call the functions recursively.
