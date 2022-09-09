```
class Solution:
def solve(self, board: List[List[str]]) -> None:
"""
Do not return anything, modify board in-place instead.
"""
if not board:
return board
vis = set()
rows = len(board)
cols = len(board[0])
def dfs(r,c,vis):
if r <= 0 or r >= rows-1 or c <= 0 or c>= cols-1 or board[r][c] == "X":
return
else:
vis.add((r,c))
board[r][c] = "X"
dfs(r+1,c,vis)
dfs(r-1,c,vis)
dfs(r,c+1,vis)
dfs(r,c-1,vis)
for r in range(rows):
for c in range(cols):
if board[r][c] == "O":
dfs(r,c,vis)
return board
```