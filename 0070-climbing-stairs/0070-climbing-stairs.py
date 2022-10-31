class Solution:
    def climbStairs(self, n: int) -> int:
        if n <= 3:
            return n
        
        first = 1
        second = 1
        
        for i in range(n-2, -1,-1):
            temp = first
            first = first+second
            second = temp
            
        return first
    