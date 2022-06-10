class Solution:
    def breakPalindrome(self, arr: str) -> str:
        if len(arr) <=1:
            return ""
        
        else:
            new_arr = []
            new_arr.extend(arr)
            for i in range(len(new_arr)//2):
                if new_arr[i] != 'a':
                    new_arr[i] = 'a'
                    return "".join(i for i in new_arr)
            
            new_arr[len(arr)-1] = 'b'
            return "".join(i for i in new_arr)

            
