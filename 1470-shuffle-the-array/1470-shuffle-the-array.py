class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        start = 0
        start_1 = n
        end = 2*n
        new_arr = []
        while start_1 < end:
            new_arr.append(nums[start])
            start+=1
            new_arr.append(nums[start_1])
            start_1+=1
        
        return new_arr
            
            