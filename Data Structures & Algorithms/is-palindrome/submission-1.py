class Solution:
    def isPalindrome(self, s: str) -> bool:
        sn = "".join(char for char in s if char.isalnum()).lower()
        i = 0
        j = len(sn)-1
        while i<j:
            if sn[i]==sn[j]:
                i+=1
                j-=1
            else:
                return False
        return True

        
            