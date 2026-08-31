class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        i=0
        n=len(needle)
        while(i<=len(haystack)):
            if haystack[i:n]==needle:
                return i 
            i+=1
            n+=1  
        return -1

        