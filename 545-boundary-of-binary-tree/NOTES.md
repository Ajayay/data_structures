if node.right:
q.append(node.right)
return arr
def rightView(self,root):
if root is not None:
arr = []
q = []
q.append(root)
while len(q):
n = len(q)
for i in range(n):
node = q.pop(0)
if i ==n:
arr.append(node.val)
if node.left:
q.append(node.left)
if node.right:
q.append(node.right)
return arr
```