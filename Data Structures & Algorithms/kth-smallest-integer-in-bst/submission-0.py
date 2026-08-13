# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        self.count = 0
        self.result = None
        def cnt(root):
            if not root:
                return
            cnt(root.left)
            self.count += 1
            if self.count == k:
                self.result = root.val
                return
            cnt(root.right)
        cnt(root)

        return self.result

        