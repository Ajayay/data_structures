# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findTarget(self, root: Optional[TreeNode], k: int) -> bool:
        
        ans = []
        return self.helper(ans,root,k)
        
        
    def helper(self,ans,root,k):
        if root is None:
            return False
        
        if root.val in ans:
            return True
        else:
            ans.append(k-root.val)
        
        lh = self.helper(ans,root.left,k)
        if lh:
            return True
        rh = self.helper(ans,root.right,k)
        if rh:
            return True
        return False