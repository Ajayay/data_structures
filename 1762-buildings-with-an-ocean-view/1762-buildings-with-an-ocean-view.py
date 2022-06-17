class Solution:
    def findBuildings(self, arr: List[int]) -> List[int]:
        
        if len(arr) == 1:
            return [0]
        if len(arr)>1:
            ans = []
            max_height = arr[len(arr)-1]
            ans.append(len(arr)-1)
            for i in range(len(arr)-2,-1,-1):
                if max_height < arr[i]:
                    max_height = arr[i]
                    ans.insert(0,i)
                else:
                    pass

            return ans
                