class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        start = 0
        arr = nums
        end = len(arr)-1
        mid =0
        
        while mid <= end:
            if arr[mid]==0:
                arr[mid],arr[start] = arr[start],arr[mid]
                mid+=1
                start+=1
            
            elif arr[mid] == 1:
                mid+=1
            else:
                arr[end],arr[mid] = arr[mid],arr[end]
                end-=1

        print(arr)
        return arr
                
        