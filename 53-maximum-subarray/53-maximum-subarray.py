class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return nums
        elif len(nums) == 1:
            return nums[0]
        else:
            max_sum = -inf
            sum_val = 0
            for i in nums:
                sum_val+=i
                if sum_val > max_sum:
                    max_sum = sum_val

                if sum_val < 0:
                    sum_val = 0

            return max_sum