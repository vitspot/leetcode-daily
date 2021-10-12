## Question:

## Diameter of Binary Tree

Given the root of a binary tree, return the length of the diameter of the tree.

The diameter of a binary tree is the length of the longest path between any two nodes in a tree. This path may or may not pass through the root.

The length of a path between two nodes is represented by the number of edges between them.

 

Example 1:

![image](https://user-images.githubusercontent.com/58622363/136731437-3d8d67b4-e986-4b14-b36c-9de0cfb25d01.png)


    Input: root = [1,2,3,4,5]
    Output: 3
    Explanation: 3 is the length of the path [4,2,1,3] or [5,2,1,3].
Example 2:

    Input: root = [1,2]
    Output: 1
 

Constraints:

    The number of nodes in the tree is in the range [1, 104].
    -100 <= Node.val <= 100

## Solutions:
1. [Submission 1](./solution1.cpp) (Cpp)