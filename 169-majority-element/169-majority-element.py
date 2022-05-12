class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        ele = self.__help(nums)
        return ele
            
        
    
    
    def __help(self,arr):
        c = 1
        m_i = 0
        for i  in range(len(arr)):
            if arr[i] == arr[m_i]:
                c+=1
            else:
                c-=1
            
            if c == 0:
                c = 1
                m_i = i
        return arr[m_i]
        
        