class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        if not heights:
            return []
        
        rows = len(heights)
        cols = len(heights[0])
        pacific_set = set()
        atlantic_set = set()
        
        
        def dfs(row,col,vis):
            vis.add((row,col))
            for (r,c) in [(1,0),(-1,0),(0,1),(0,-1)]:
                new_row = r+row
                new_col = c+col
                if new_row < 0 or new_row>=rows or new_col <0 or new_col >= cols:
                    continue
                if (new_row,new_col) in vis:
                    continue
                if heights[new_row][new_col] < heights[row][col]:
                    continue
                dfs(new_row,new_col,vis)
        
        
        
        for r in range(rows):
            dfs(r,0,pacific_set)
            dfs(r,cols-1,atlantic_set)
        for c in range(cols):
            dfs(0,c,pacific_set)
            dfs(rows-1,c,atlantic_set)
            
            
        return list(pacific_set.intersection(atlantic_set))