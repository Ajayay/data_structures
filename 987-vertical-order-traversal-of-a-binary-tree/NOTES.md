```
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
def verticalTraversal(self, root: Optional[TreeNode]) -> List[List[int]]:
if root!= None:
root.nums = 0
map = {}
q = []
q.append(root)
while len(q):
node = q.pop(0)
if node.nums not in map:
map[node.nums] = [node.val]
else:
lst = map[node.nums]
lst.append(node.val)
map[node.nums] = lst
if node.left:
node.left.nums = node.nums-1
q.append(node.left)
if node.right:
node.right.nums = node.nums +1
q.append(node.right)
ans = []
for i in sorted(map):
if len(map[i]) > 1:
map[i].sort()
ans.append(map[i])
return ans
```