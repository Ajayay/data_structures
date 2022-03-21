class Solution:
    def getModifiedArray(self, length: int, updates: List[List[int]]) -> List[int]:
        arr = [0] * length
        for i in updates:
            start = i[0]
            end = i[1]
            increment = i[2]
            arr[start]+=increment
            if end < length-1:
                arr[end+1] -=increment
                
        val = 0
        for i in range(len(arr)):
            val+=arr[i]
            arr[i] = val
            
                
        return arr
            