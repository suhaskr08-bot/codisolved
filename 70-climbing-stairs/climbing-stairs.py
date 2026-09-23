class Solution:
    def check(self,n,dp):
        if n==0 or n==1:
            return 1 
        if dp[n]!=-1:
            return dp[n]
        dp[n]=self.check(n-1,dp)+self.check(n-2,dp)
        return dp[n]
    def climbStairs(self, n: int) -> int:
        dp=[-1]*(n+1)
        return self.check(n,dp)