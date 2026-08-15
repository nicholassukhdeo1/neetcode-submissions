# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        # i want to get the maxdepth

        # we traverse the left and the right branch]

        self.depth = 0
        self.result = 0

        def depth(root,depth1: int):
            if not root:
                return depth1
            
            leftDepth = depth(root.left,depth1+1)
            rightDepth = depth(root.right,depth1+1)

            self.result = max(leftDepth, rightDepth)
            return self.result

        depth(root,0)
        return self.result
