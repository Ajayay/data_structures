```
class Solution:
def highFive(self, items: List[List[int]]) -> List[List[int]]:
dictt = {}
for i in items:
id_i = i[0]
mrks_i = i[1]
if id_i not in dictt:
temp = []
temp.append(mrks_i)
dictt[id_i] = temp
else:
mrks_lst = dictt.get(id_i)
mrks_lst.append(mrks_i)
ans = []
for key,val in dictt.items():
inner_lst = []
val.sort(reverse = True)
sum_val  = sum(val[:5])
avg = sum_val//5
# print(key,avg)
inner_lst.append(key)
inner_lst.append(avg)
ans.append(inner_lst)
return ans
```