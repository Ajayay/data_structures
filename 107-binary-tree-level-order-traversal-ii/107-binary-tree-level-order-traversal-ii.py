# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrderBottom(self, root: Optional[TreeNode]) -> List[List[int]]:
        
        ans = []
        
        if root is None:
            return ans
        
        def helper(node,level):
            if len(ans)== level:
                ans.append([])
                
            ans[level].append(node.val)
            if node.left:
                helper(node.left,level+1)
            if node.right:
                helper(node.right,level+1)
        
        
        
        helper(root,0)
        return ans[::-1]