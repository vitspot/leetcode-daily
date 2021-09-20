#   Find Winner on a Tic Tac Toe Game

Tic-tac-toe is played by two players A and B on a 3 x 3 grid.

Here are the rules of Tic-Tac-Toe:

Players take turns placing characters into empty squares (" ").
The first player A always places "X" characters, while the second player B always places "O" characters.
"X" and "O" characters are always placed into empty squares, never on filled ones.
The game ends when there are 3 of the same (non-empty) character filling any row, column, or diagonal.
The game also ends if all squares are non-empty.
No more moves can be played if the game is over.
Given an array moves where each element is another array of size 2 corresponding to the row and column of the grid where they mark their respective character in the order in which A and B play.

Return the winner of the game if it exists (A or B), in case the game ends in a draw return "Draw", if there are still movements to play return "Pending".

You can assume that moves is valid (It follows the rules of Tic-Tac-Toe), the grid is initially empty and A will play first.

 

### Example 1:

        Input: moves = [[0,0],[2,0],[1,1],[2,1],[2,2]]
        
        Output: "A"

### Explanation: 

            "A" wins, he always plays first.

            "X  "    "X  "    "X  "    "X  "    "X  "

            "   " -> "   " -> " X " -> " X " -> " X "

            "   "    "O  "    "O  "    "OO "    "OOX"

### Example 2:

    Input: moves = [[0,0],[1,1],[0,1],[0,2],[1,0],[2,0]]

    Output: "B"


### Explanation:

    "B" wins.

    "X  "    "X  "    "XX "    "XXO"    "XXO"    "XXO"

    "   " -> " O " -> " O " -> " O " -> "XO " -> "XO " 

    "   "    "   "    "   "    "   "    "   "    "O  "




**Reference**: https://leetcode.com/explore/challenge/card/september-leetcoding-challenge-2021/638/week-3-september-15th-september-21st/3981/

## Solutions
1. [Submission 1](./solution.cpp)
1. [Submission 2](./solution2.cpp)

```cpp
string tictactoe(vector<vector<int>> &moves)
{
    if (moves.size() <= 2) return "Pending";

    int n = 3;
    vector<int> rows(3, 0);
    vector<int> cols(3, 0);
    int d1 = 0;
    int d2 = 0;

    int turnA = 1;
    for (auto i : moves) {
        int x = i[0];
        int y = i[1];

        rows[x] += turnA;
        cols[y] += turnA;

        if (x == y) d1 += turnA;
        if (x + y == n - 1) d2 += turnA;

        // check if its a winning condition
        if (
            abs(rows[x]) == n ||
            abs(cols[y]) == n ||
            abs(d1) == n ||
            abs(d2) == n)
        {
            return turnA == 1 ? "A" : "B";
        }
        turnA = -1 * turnA;
    }

    if (moves.size() < 9) return "Pending";
    return "Draw";
}
```

