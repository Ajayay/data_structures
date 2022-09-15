class Solution:
    def wallsAndGates(self, rooms: List[List[int]]) -> None:
        """
        Do not return anything, modify rooms in-place instead.
        """
    
        if not rooms:
            return rooms
        INF =  2147483647 
        rows = len(rooms)
        cols = len(rooms[0])
        q = []
        for r in range(rows):
            for c in range(cols):
                if rooms[r][c] == 0:
                    q.append((r,c))
                    
        
        
        while q:
            row,col = q.pop(0)
            if row > 0 and rooms[row-1][col] == INF:
                rooms[row-1][col] = rooms[row][col]+1
                q.append((row-1,col))
            
            if row < rows-1 and rooms[row+1][col] == INF:
                rooms[row+1][col] = rooms[row][col]+1
                q.append((row+1,col))
                
                
            if col > 0 and  rooms[row][col-1] == INF:
                rooms[row][col-1] = rooms[row][col]+1
                q.append((row,col-1))
                
            if col < cols-1 and  rooms[row][col+1] == INF:
                rooms[row][col+1] = rooms[row][col]+1
                q.append((row,col+1))