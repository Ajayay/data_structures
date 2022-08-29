class Solution:
    def breakPalindrome(self, S: str) -> str:
        
        
        for i in range(len(S) // 2):
            if S[i] != 'a':
                return S[:i] + 'a' + S[i + 1:]
        if S[:-1]:
            return S[:-1]+"b"
        else:
            return ""
        # return S[:-1] + 'b' if S[:-1] else ''
        
        
        
                
                