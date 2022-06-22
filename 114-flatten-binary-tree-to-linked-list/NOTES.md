```
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
def flatten(self, root: Optional[TreeNode]) -> None:
"""
Do not return anything, modify root in-place instead.
"""
if root is not None:
cur = root
self.__helper(root,cur)
def __helper(self,root,cur):
if root is not None:
if cur is None:
cur = root
else:
cur.right = root
cur.left = None
if root.left:
self.__helper(root.left,cur)
if root.right:
self.__helper(root.right,cur)
```