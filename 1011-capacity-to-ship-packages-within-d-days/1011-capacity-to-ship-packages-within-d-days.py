class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        def feasible(capacity):
            day = 1
            local = 0
            for w in weights:
                local+=w
                if local>capacity:
                    local = w
                    day+=1
                    if day>days:
                        return False
            return True
            
                
        left, right = max(weights), sum(weights)
        while left < right:
            mid = left + (right-left)//2
            if feasible(mid):
                right = mid
            else:
                left = mid + 1

        return left