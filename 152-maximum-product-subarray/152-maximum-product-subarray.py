class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        
        res =nums[0]
        prod1 = nums[0]
        prod2 = nums[0]
        
        for i in range(1,len(nums)):
            
            temp = max(nums[i],max(prod1*nums[i],prod2*nums[i]))
            prod2 = min(nums[i],min(prod1*nums[i],prod2*nums[i]))
            prod1 = temp
            
            res = max(res,prod1)
            
        return res