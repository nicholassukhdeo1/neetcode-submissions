# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        # array method
        self.res = []

        def indexer(root):
            if not root:
                return
            self.res.append(root.val)
            indexer(root.left)
            indexer(root.right)
        indexer(root)
        self.res.sort()

        return self.res[k-1]