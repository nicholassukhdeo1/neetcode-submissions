# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        # you want to swap the level below, then move a level down

        # check first if you can even move a level down

        if not root:
            return

        # swap level below

        root.left, root.right = root.right, root.left

        self.invertTree(root.left)
        self.invertTree(root.right)


        return root

