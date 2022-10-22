class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        
        arr = []
        
        for i in range(len(text1)+1):
            arr.append([0]*(len(text2)+1))
            
        
        for row in range(len(text1)-1,-1,-1):
            for col in range(len(text2)-1,-1,-1):
                if text1[row] == text2[col]:
                    arr[row][col] = 1 + arr[row+1][col+1]
                else:
                    arr[row][col] = max(arr[row][col+1], arr[row+1][col])
                    
        return arr[0][0]