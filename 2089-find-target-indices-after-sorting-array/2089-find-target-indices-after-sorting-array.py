class Solution:
    def targetIndices(self, nums: List[int], target: int) -> List[int]:
        if len(nums) == 1 and nums[0] == target:
            return [0]
        
        sorted_arr = sorted(nums,reverse=False)
        # print(sorted_arr)
        start = 0
        end = len(sorted_arr)-1
        ans_arr = []
        ans = self.binary_search(start,end,sorted_arr,target,True)
        # print(ans)
        if ans == -1:
            return []
        ans_arr.append(ans)
        ans1 = self.binary_search(start,end,sorted_arr,target,False)
        if sorted_arr[ans1] == sorted_arr[ans1-1]:
            for i in range(ans+1,ans1+1):
                ans_arr.append(i)
        return ans_arr
        
        
        
    def binary_search(self,start,end,sorted_arr,target,is_first):
        while start <=end:
            # print(start,end)
            mid = (start+end)//2
            # print(mid)
            if sorted_arr[mid] == target:
                if is_first:
                    if start == mid or sorted_arr[mid-1] < sorted_arr[mid]:
                        return mid
                    end = mid-1
                else:
                    
                    if end == mid or sorted_arr[mid+1] > sorted_arr[mid]:
                        return mid
                    start = mid+1
            if sorted_arr[mid] > target:
                end = mid-1
            if sorted_arr[mid] < target:
                start = mid +1
                
        return -1
                    
                    
                    