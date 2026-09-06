class Solution:
    def isPalindrome(self, s: str) -> bool:
        s=s.lower()
        ans=""
        for i in s:
            if not i.isalnum():
                continue 
            ans+=i
        return ans==ans[::-1]
                
            
