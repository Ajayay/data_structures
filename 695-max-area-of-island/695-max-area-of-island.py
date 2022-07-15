class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        
        rows = len(grid)
        cols = len(grid[0])
        max_area = 0
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    max_area = max(max_area,self.helper(r,c,grid,rows,cols))
                    
        return max_area
    
    def helper(self,r,c,grid,rows,cols):
        if (0<=r< rows and 0<=c < cols and grid[r][c] == 1):
            grid[r][c] = 0
            return 1 + self.helper(r-1,c,grid,rows,cols)+self.helper(r+1,c,grid,rows,cols)+self.helper(r,c-1,grid,rows,cols)+self.helper(r,c+1,grid,rows,cols)
        return 0