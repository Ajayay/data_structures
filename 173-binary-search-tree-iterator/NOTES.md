**BST Iterator for pre-order traversal**
```
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class BSTIterator:
​
def __init__(self, root: Optional[TreeNode]):
self.root = root
self.prev = None
self.flatten_bst(self.root)
self.curr = self.root
self.hsnxt = self.root
self.ans = 0
​
def flatten_bst(self,root):
if root == None:
return None
self.flatten_bst(root.right)
self.flatten_bst(root.left)
root.right = self.prev