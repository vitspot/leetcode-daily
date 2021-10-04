## Question:

## Island Perimeter

You are given row x col grid representing a map where grid[i][j] = 1 represents land and grid[i][j] = 0 represents water.

Grid cells are connected horizontally/vertically (not diagonally). The grid is completely surrounded by water, and there is exactly one island (i.e., one or more connected land cells).

The island doesn't have "lakes", meaning the water inside isn't connected to the water around the island. One cell is a square with side length 1. The grid is rectangular, width and height don't exceed 100. Determine the perimeter of the island.

Example 1:

![image](https://user-images.githubusercontent.com/58622363/135891529-31576630-52ec-43b6-a6fe-5c2212a00276.png)

    Input: grid = [[0,1,0,0],[1,1,1,0],[0,1,0,0],[1,1,0,0]]
    Output: 16
    Explanation: The perimeter is the 16 yellow stripes in the image above.
Example 2:

    Input: grid = [[1]]
    Output: 4
Example 3:

    Input: grid = [[1,0]]
    Output: 4
 

Constraints:

    row == grid.length
    col == grid[i].length
    1 <= row, col <= 100
    grid[i][j] is 0 or 1.
    There is exactly one island in grid.

## Solutions:
1. [Submission 1](./solution1.cpp) (Cpp)
2. [Submission 2](./solution2.py) (Py)
3. [Submission 3](./solution3.py) (Py)