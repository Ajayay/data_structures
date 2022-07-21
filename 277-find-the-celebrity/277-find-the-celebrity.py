# The knows API is already defined for you.
# return a bool, whether a knows b
# def knows(a: int, b: int) -> bool:

class Solution:
    def findCelebrity(self, n: int) -> int:
        celeb = 0
        ans = True
        for i in range(1,n):
            if knows(celeb,i):
                celeb = i
        
        for j in range(n):
            if celeb == j:
                continue
            if knows(celeb,j) or not knows(j,celeb):
                ans = False
            
        
        if ans:
            return celeb
        else:
            return -1