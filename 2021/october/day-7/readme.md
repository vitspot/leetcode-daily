## Question:

## Word Search

Given an m x n grid of characters board and a string word, return true if word exists in the grid.

The word can be constructed from letters of sequentially adjacent cells, where adjacent cells are horizontally or vertically neighboring. The same letter cell may not be used more than once.

 

Example 1:

![image](https://user-images.githubusercontent.com/58622363/136426223-941fd0b4-0c16-49fa-a7d2-c8f239b3246e.png)

    Input: board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "ABCCED"
    Output: true

Example 2:

![image](https://user-images.githubusercontent.com/58622363/136426209-943bcce5-3800-4b9a-8898-c5f2d84f7691.png)

    Input: board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "SEE"
    Output: true

Example 3:

    
![image](https://user-images.githubusercontent.com/58622363/136426182-b3990509-1de0-417a-879a-956c20dc1ceb.png)

    Input: board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "ABCB"
    Output: false
 

Constraints:

    m == board.length
    n = board[i].length
    1 <= m, n <= 6
    1 <= word.length <= 15
    board and word consists of only lowercase and uppercase English letters.
 

Follow up: Could you use search pruning to make your solution faster with a larger board?

## Solutions:
1. [Submission 1](./solution1.cpp) (Cpp)
2. [Submission 2](./solution2.py) (Py)