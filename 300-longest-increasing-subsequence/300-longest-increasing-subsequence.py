class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        
        ans = []
        ans.append(1)
        
        for i in range(1,len(nums)):
            maxVal = 0
            for j in range(i-1,-1,-1):
                if nums[j] < nums[i]:
                    maxVal = max(maxVal,ans[j])
                    
                    
            ans.append(maxVal + 1)
            
        
        return max(ans)