class Solution:
    def suggestedProducts(self, products: List[str], searchWord: str) -> List[List[str]]:
        ans = []
        products.sort()
        # searched_word_len = len(searchWord)
        for j in range(len(searchWord)):
            temp = []
            for i in products:
                if searchWord[:j+1] == i[:j+1]:
                    if len(temp)<3:
                        temp.append(i)
                    else:
                        break
            # print(temp)
            ans.append(temp)
        
        return ans
        