#https://leetcode.com/problems/climbing-stairs/
w={1:1, 2:2}
class Solution:
    @cache
    def climbStairs(self,n:int)->int:
        if n in w:
            return w[n]
        x=0
        x+=self.climbStairs(n-1) 
        x+=self.climbStairs(n-2)
        w[n]=x
        return x
