
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        if not grid:
            return 
        
        rows= len(grid)
        cols = len(grid[0])
        q = []
        count_fresh = 0
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 2:
                    q.append((r,c))
                elif grid[r][c] == 1:
                    count_fresh+=1
                    
        if count_fresh == 0:
            return 0
        count = 0
        while len(q) and count_fresh>0:
            count+=1
            size_q = len(q)
            for sz in range(size_q):
                rrow,rcol= q.pop(0)
                for x,y in [(1,0),(0,1),(-1,0),(0,-1)]:
                    new_row , new_col = rrow+x , rcol+y
                    if new_row>=0 and new_row < rows and new_col >=0 and new_col<cols:
                        if grid[new_row][new_col] == 1:
                            grid[new_row][new_col] = 2
                            q.append((new_row,new_col))
                            count_fresh-=1
            # count+=1
        if count_fresh == 0:
            return count
        else:
            return -1
                
                       