# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def makeTrees(start: int, end: int):
    if start > end:
        return [None]
    lst = []
    for i in range(start, end+1):
        leftSubtree = makeTrees(start, i-1)
        rightSubtree = makeTrees(i+1, end)
        for j in leftSubtree:
            for k in rightSubtree:
                newNode = TreeNode(i, j, k)
                lst.append(newNode)
    return lst


class Solution:
    def generateTrees(self, n: int) -> List[Optional[TreeNode]]:
        return makeTrees(1, n)
