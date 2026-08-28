class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        if s==s[::-1]:
            return s
        maximum_pali=""
        maxi=0
        for i in range(len(s)):
            for j in range(i+1,len(s)+1):
                 new=s[i:j]
                 if new==new[::-1] and len(new)>maxi:
                    maximum_pali=new
                    maxi=len(new)
        return maximum_pali
        
        