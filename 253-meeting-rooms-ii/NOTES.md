**sample test cases passed**
​
```
class Solution:
def minMeetingRooms(self, intervals: List[List[int]]) -> int:
arr = intervals
arr.sort(key = lambda x: x[0])
print(arr)
room  = 0
e = 10000
for i in range(len(arr)):
a = arr[i]
if a[0] < e:
room+=1
e = a[1]
else:
if a[1] > e:
e = a[1]
return room
```