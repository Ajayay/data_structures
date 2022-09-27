class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        
        start = []
        end = []
        
        for i in range(len(intervals)):
            start.append(intervals[i][0])
            end.append(intervals[i][1])
            
        start.sort()
        end.sort()
        
        rooms = 0
        endm = 0
        for i in range(len(start)):
            if start[i]<end[endm]:
                rooms+=1
            else:
                endm+=1
                
        return rooms