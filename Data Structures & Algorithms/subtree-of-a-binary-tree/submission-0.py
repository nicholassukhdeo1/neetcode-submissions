# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        # we need base cases / edge cases

        # if our subtree is Null, then its always a subtree
        if not subRoot:
            return True
        # if our tree is Null, it cant have a subtree
        if subRoot and not root:
            return False

        # if our tree and subTree are the same thing.. return True

        if self.sameTree(root,subRoot):
            return True

        # and then we do our recursive call to assure that we check all nodes within the tree
        # to see if theyre the same value

        return (self.isSubtree(root.left, subRoot)) or (self.isSubtree(root.right, subRoot))

        # a recursive call

    def sameTree(self, root, subRoot):
        # base cases, when do we know its the same tree.. or not?

        #if both are null
        if not root and not subRoot:
            return True
        # if one is None, and the other isnt
        if root and not subRoot:
            return False
        if subRoot and not root:
            return False
        
        # then if the values are equal
        if (root.val == subRoot.val):
            # for ALL nodes.
            return self.sameTree(root.left, subRoot.left) and self.sameTree(root.right, subRoot.right)
        return False
