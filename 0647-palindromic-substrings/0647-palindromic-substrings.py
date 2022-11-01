class Solution:
    def countSubstrings(self, s: str) -> int:
        resCount = 0
        for i in range(len(s)):
            l,r = i,i+1
            while l>= 0  and r <= len(s)-1 and s[l] == s[r]:
                resCount +=1
                l-=1
                r+=1

            # else:
            l,r = i,i
            while l>= 0  and r <= len(s)-1 and s[l] == s[r]:
                resCount +=1
                l-=1
                r+=1

        return resCount