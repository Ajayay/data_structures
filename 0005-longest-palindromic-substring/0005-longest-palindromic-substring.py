class Solution:
    def longestPalindrome(self, s: str) -> str:
        resLen = 0
        res = ""
        for i in range(len(s)):
            # if len(s)%2 == 0:
            l,r = i,i+1
            while l>= 0  and r <= len(s)-1 and s[l] == s[r]:
                if r-l+1 > resLen:
                    resLen = r-l+1
                    res = s[l:r+1]

                l-=1
                r+=1

            # else:
            l,r = i,i
            while l>= 0  and r <= len(s)-1 and s[l] == s[r]:
                if r-l+1 > resLen:
                    resLen = r-l+1
                    res = s[l:r+1]

                l-=1
                r+=1

        return res