class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        
        arr = []
        i = 0
        
        while i < len(intervals) and intervals[i][0] < newInterval[0]:
            arr.append(intervals[i])
            i+=1
            
        
        if not arr or arr[-1][1] < newInterval[0]:
            arr.append(newInterval)
        else:
            arr[-1][1] = max(arr[-1][1], newInterval[1])
            
            
        while i < len(intervals):
            start = intervals[i][0]
            end = intervals[i][1]
            # i+=1
            
            if arr[-1][1] < start:
                arr.append(intervals[i])
            else:
                arr[-1][1] = max(arr[-1][1], intervals[i][1])
            i+=1
        return arr
            