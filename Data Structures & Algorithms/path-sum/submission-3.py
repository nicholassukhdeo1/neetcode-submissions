# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        

        self.res = False


        def helper(root,sum_):

            if root is None:
                return False

            # do

            sum_ += root.val
            if not root.left and not root.right:
                return sum_ == targetSum


            # recurse

            return helper(root.left,sum_) or helper(root.right,sum_)


        return helper(root,0)
