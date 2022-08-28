class Solution:
    def isRobotBounded(self, instructions: str) -> bool:
        
        direction = "N"
        x = 0
        y = 0
        
        for i in instructions:
            
            if i == "G":
                if direction == "N":
                    y+=1
                elif direction == "S":
                    y-=1
                elif direction == "E":
                    x+=1
                else:
                    x-=1
                    
            elif i == "L":
                if direction == "N":
                    direction = "W"
                elif direction == "S":
                    direction = "E"
                elif direction == "E":
                    direction = "N"
                else:
                    direction = "S"
            elif i == "R":
                if direction == "N":
                    direction = "E"
                elif direction == "S":
                    direction = "W"
                elif direction == "E":
                    direction = "S"
                else:
                    direction = "N"
        if x==0 and y ==0:
            return True
        if direction == "N":
            return False
        return True