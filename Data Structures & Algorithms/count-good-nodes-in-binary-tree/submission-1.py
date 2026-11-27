# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        


        def DFS(root,cur_max):

            if root is None:
                return 0

            
            if root.val >= cur_max:
                count = 1 + DFS(root.left,root.val) + DFS(root.right,root.val)

            
            else:
                count = DFS(root.left,cur_max) + DFS(root.right,cur_max)


            return count



        return DFS(root,-101)
