class Solution:
    def camelMatch(self, queries: List[str], pattern: str) -> List[bool]:
        res = []
        new_pattern = []
        new_pattern.extend(pattern)
        for i in queries:
            ans = self.match(i, new_pattern)
            if ans != None:
                res.append(ans)
        
        return res
                
                
    
    def match(self, query, pattern):
        
        j = 0
        for i in range(len(query)):
            if j > len(pattern):
                break
                
            if j < len(pattern)  and query[i] == pattern[j]:
                j+=1
            elif query[i] >= 'A' and query[i] <= 'Z':
                return False
            
            
                
        return j == len(pattern)