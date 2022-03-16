class Solution:
    def restoreString(self, s: str, indices: List[int]) -> str:
        dict = {}
        for i in range(len(indices)):
            if dict.get(indices[i]) is None:
                dict[indices[i]] = s[i]
            else:
                pass
            
        s = ""
        for i in sorted(dict.keys()):
            s +=dict.get(i)
            # print(dict.get(i) , end = " ")
        
        return s
            