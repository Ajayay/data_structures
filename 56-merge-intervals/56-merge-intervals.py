class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key = lambda x : x[0])
        arr = []
        i = 0
        start = intervals[i][0]
        end = intervals[i][1]
        arr.append([start,end])
        i+=1
        while i < len(intervals):
            if arr[-1][1] < intervals[i][0]:
                arr.append(intervals[i])
            else:
                arr[-1][1] = max(arr[-1][1], intervals[i][1])
            i+=1
        
        return arr