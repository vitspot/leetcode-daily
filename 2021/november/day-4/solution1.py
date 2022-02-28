class Solution:
        def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
            stack = deque([(root,False)])
            
            result = 0
            
            while stack:
                node,isleft = stack.popleft()
                if not node: continue
                if not (node.left or node.right) and isleft:
                    result+=node.val
                    continue
                stack.append((node.left,True))
                stack.append((node.right,False))
            
            return result