class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        start = 0
        end = len(nums)-1
        ans = 0
        arr = nums
        k = target
        while start<=end:
            
            mid = (start +end)//2
            
            if arr[mid] == k:
                return mid
            elif arr[mid]>k:
                end = mid-1
            else:
                start=mid+1
        
        return start