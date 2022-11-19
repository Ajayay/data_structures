class Solution:
    def uniquePaths(self, r: int, c: int) -> int:
        if r==1:
            return 1
        if c == 1:
            return 1
        row = [1]*c
        for i in range(r-1):
            new_row = [1]*c
            for j in range(c-2,-1,-1):
                new_row[j] = new_row[j+1]+row[j]
            row = new_row
            
        return new_row[0]