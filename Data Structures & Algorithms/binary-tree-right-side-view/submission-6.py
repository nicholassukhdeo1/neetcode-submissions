# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:

        self.res = []

        if root is None:
            return self.res

        self.res.append(root.val)

        

        def DFS(root,depth):

            if root is None:
                return 0

            # if right has been added at this depth.. dont add

            # start adding left the moment its bigger than right_depth

            # print(f"curr_node val is: {root.val}")

            if depth == len(self.res):
                self.res.append(root.val)


            if root.right:
                DFS(root.right,depth+1) 
            if root.left:
                DFS(root.left, depth+1)




            

        DFS(root,0)
        
        return self.res