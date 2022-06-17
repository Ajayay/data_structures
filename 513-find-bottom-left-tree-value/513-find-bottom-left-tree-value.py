# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findBottomLeftValue(self, root: Optional[TreeNode]) -> int:
        if root is not None:
            q = []
            ans = []
            q.append(root)
            while len(q):
                size = len(q)
                for i in range(size):
                    node = q.pop(0)
                    if i == 0:
                        ans.append(node.val)
                        
                    if node.left:
                        q.append(node.left)
                        
                    if node.right:
                        q.append(node.right)
            print(ans)
            return ans[-1]
        else:
            return []