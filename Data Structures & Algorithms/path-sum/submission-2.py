# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        # what are the base cases?

        self.result = False

        def sum(root,temp_sum):
            if not root:
                return False

            temp_sum += root.val

            if not root.left and not root.right:
                if temp_sum == targetSum:
                    return True


            

            if sum(root.left, temp_sum):
                return True
            if sum(root.right, temp_sum):
                return True


            temp_sum -= root.val

            return False


        return sum(root, 0)