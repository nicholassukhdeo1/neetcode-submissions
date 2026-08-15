class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        in_map = {val: i for i, val in enumerate(inorder)}
        
        def helper(p_start, p_end, i_start, i_end):
            if p_start > p_end:
                return None
            
            root_val = preorder[p_start]
            root = TreeNode(root_val)
            mid = in_map[root_val]
            left_size = mid - i_start
            
            root.left = helper(p_start + 1, p_start + left_size, i_start, mid - 1)
            root.right = helper(p_start + left_size + 1, p_end, mid + 1, i_end)
            return root
            
        return helper(0, len(preorder) - 1, 0, len(inorder) - 1)