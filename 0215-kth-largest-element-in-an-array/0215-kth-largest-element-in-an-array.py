class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        
        def partition(left,right):
            pivot_index = right
            
            j = left
            for i in range(left,right):
                if nums[i]<nums[pivot_index]:
                    nums[i],nums[j] = nums[j],nums[i]
                    j+=1
            
            nums[j],nums[right] = nums[right],nums[j]
            return j
        
        
        def selectSort(left,right,kth_smallest):
            if left == right:
                return nums[left]
            
            pivot_index = partition(left,right)
            if pivot_index == kth_smallest:
                return nums[pivot_index]
            elif pivot_index>kth_smallest:
                return selectSort(left,pivot_index-1,kth_smallest)
            else:
                return selectSort(pivot_index+1,right,kth_smallest)
        
        return selectSort(0,len(nums)-1,len(nums)-k)