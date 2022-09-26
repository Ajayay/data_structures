class Solution:
    def canAttendMeetings(self, intervals: List[List[int]]) -> bool:
        if not intervals:
            return True
        intervals.sort(key = lambda x: x[0])
        start = intervals[0][0]
        end = intervals[0][1]
        i = 1
        while i < len(intervals):
            if end>intervals[i][0]:
                return False
            else:
                end = intervals[i][1]
            i+=1
        return True
        
        