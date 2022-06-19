# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        if root != None:
            q = []
            root.idx = 0
            q.append(root)
            ans = 0
            while len(q):
                n = len(q)
                minVal = q[0].idx
                first = 0
                last = 0
                for i in range(n):
                    curr_id = q[0].idx - minVal
                    node = q.pop(0)
                    
                    if i == 0:
                        first = curr_id
                        
                    if i == n-1:
                        last = curr_id
                        
                    
                    if node.left:
                        node.left.idx = 2*(node.idx) + 1
                        q.append(node.left)
                    
                    if node.right:
                        node.right.idx = 2 * (node.idx)+2
                        q.append(node.right)
                        
                ans = max(ans, last-first+1)
            return ans
                
                