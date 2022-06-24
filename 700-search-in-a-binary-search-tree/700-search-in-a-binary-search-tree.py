# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def searchBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        if root is None:
            return None
            
        if root.val == val:
            return root
        if root is not None:
            if val  < root.val:
                root = self.searchBST(root.left, val)
        if root is not None:
            if val > root.val:
                root = self.searchBST(root.right,val)

        return root
        