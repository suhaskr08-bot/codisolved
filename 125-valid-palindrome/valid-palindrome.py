class Solution:
    def isPalindrome(self, s: str) -> bool:
        s=s.lower()
        ans=""
        for i in s:
            if i in " [],*:./@!#$%^&*()_-+=\'\"{}?><;\\`":
                continue 
            ans=i+ans
        return ans==ans[::-1]
                
            
