class Solution:
    def rotateString(self, s: str, goal: str) -> bool:
         return len(s) == len(goal) and goal in s + s
#         if (len(s) != len(goal)):
#             return False
#         arr = []
#         for i in s:
#             arr.append(i)
#         mid = (0 + (len(arr) - 1)) // 2
#         while arr[0] != goal[0]:
#             arr = self._rotateString(arr, 0, mid)
#             arr = self._rotateString(arr, mid + 1, (len(arr) - 1))
#             arr = self._rotateString(arr, 0, len(arr) - 1)

#         print(arr)
#         for i in range(len(arr)):
#             if arr[i] != goal[i]:
#                 return False
#         return True

#     def _rotateString(self, arr, start, end):
#         while start<end:
#             arr[start], arr[end] = arr[end], arr[start]
#             start+=1
#             end-=1

#         return arr
