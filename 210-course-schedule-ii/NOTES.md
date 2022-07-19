```
class Solution:
def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
if len(prerequisites) == 0:
lst = []
for i in range(numCourses):
lst.append(i)
return lst
adj_lst = defaultdict(list)
for i in prerequisites:
i.sort(reverse = True)
print(prerequisites)
for j,k in prerequisites:
adj_lst[k].append(j)
print(adj_lst)
visited = []
start = 0
visited.append(start)
stack = []
​
def helper(visited, stack, start, adj_lst):
for i in adj_lst[start]:
if i not in visited:
visited.append(i)
helper(visited,stack,i,adj_lst)
​
stack.append(start)
​
​
helper(visited, stack, start, adj_lst)
res = []
print(stack)
for i in stack[::-1]:
res.append(i)
if numCourses>=len(stack):
ans = res[:numCourses]
ans.sort()
return ans
else:
return []
```