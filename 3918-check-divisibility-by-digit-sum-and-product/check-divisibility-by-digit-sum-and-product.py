class Solution:
    def checkDivisibility(self, n: int) -> bool:
        summ=0
        pro=1
        ans=n
        while(n!=0):
             
            summ+=n%10
            pro*=n%10
            n=n//10
        if ans%(summ+pro)==0:
            return True 
        else:
            return False