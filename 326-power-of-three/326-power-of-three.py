class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        if n == 1:
            return True
        k = 3
        while k < n:
            k = k * 3
            
        if k == n:
            return True
        else:
            return False
            