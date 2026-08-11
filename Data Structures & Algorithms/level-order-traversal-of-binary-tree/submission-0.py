# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        
        # base case

        # recursive call (what are we solving here)

        # return a list of lists, where each list in the list is a level
        res = []

        if not root:
            return res

        queue = deque()

        queue.append(root)
        
        level = []
        level.append(root.val)

        while len(queue) > 0:
            res.append(level)
            level = []

            for i in range(len(queue)):
                curr_num = queue.popleft()
                if curr_num.left:
                    queue.append(curr_num.left)
                    level.append(curr_num.left.val)
                if curr_num.right:
                    queue.append(curr_num.right)
                    level.append(curr_num.right.val)

        return res
        