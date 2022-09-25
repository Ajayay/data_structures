class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        
        intervals.sort(key = lambda x:x[0])
        
        arr = []
        start = intervals[0][0]
        end = intervals[0][1]
        i = 1
        arr.append([start,end])
        while i<len(intervals):
            
            if arr[-1][1]<intervals[i][0]:
                arr.append(intervals[i])
            else:
                arr[-1][1] = max(arr[-1][1], intervals[i][1])
            i+=1
        return arr
        
        