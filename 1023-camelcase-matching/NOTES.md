```
class Solution:
def camelMatch(self, queries: List[str], pattern: str) -> List[bool]:
i = 0
st = ""
ans = []
res = []
while i < len(pattern):
while i <len(pattern) and not pattern[i].isupper():
st+=pattern[i]
i+=1
if i <len(pattern) and pattern[i].isupper():
if i != 0:
ans.append(st)
st = ""
st= pattern[i]
i+=1
else:
st = pattern[i]
i+=1
if st != "":
ans.append(st)
for i in queries:
if
```