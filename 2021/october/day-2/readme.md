##  Dungeon Game:

The demons had captured the princess and imprisoned her in the bottom-right corner of a dungeon. The dungeon consists of m x n rooms laid out in a 2D grid. Our valiant knight was initially positioned in the top-left room and must fight his way through dungeon to rescue the princess.

The knight has an initial health point represented by a positive integer. If at any point his health point drops to 0 or below, he dies immediately.

Some of the rooms are guarded by demons (represented by negative integers), so the knight loses health upon entering these rooms; other rooms are either empty (represented as 0) or contain magic orbs that increase the knight's health (represented by positive integers).

To reach the princess as quickly as possible, the knight decides to move only rightward or downward in each step.

Return the knight's minimum initial health so that he can rescue the princess.

Note that any room can contain threats or power-ups, even the first room the knight enters and the bottom-right room where the princess is imprisoned.

![image](https://user-images.githubusercontent.com/58622363/135742212-0ec85c88-c72b-4472-bf4b-f81317c266dc.png)


Example 2:

    Input: dungeon = [[0]]
    Output: 1
    
Constraints:

    m == dungeon.length
    n == dungeon[i].length
    1 <= m, n <= 200
    -1000 <= dungeon[i][j] <= 1000


## Solutions:
1. [Submission 1](./solution1.py) (Py)
2. [Submission 2](./solution2.py) (Py)
