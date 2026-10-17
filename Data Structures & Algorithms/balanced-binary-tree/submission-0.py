# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:


        self.isBalanced = True

        def dfs(curr):
            if curr is None:
                return 0

            left_height = 1 + dfs(curr.left)
            right_height = 1 + dfs(curr.right)

            if abs(left_height - right_height) > 1:
                self.isBalanced = False


            return max(left_height,right_height)
        


        dfs(root)

        return self.isBalanced