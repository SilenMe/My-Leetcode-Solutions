#immediately two appoaches came into mind, sorting and hashMap. Looks like sorting is faster but there is not much difference. I'm going with hashMap sol
class Solution:
    def longestSquareStreak(self, nums: List[int]) -> int:
        d={}
        for i in nums:
            d[i]=i*i
        sol=-1
        for i in d:
            temp=i*i
            t=-1
            while True:
                if temp in d:
                    temp=temp*temp
                    t=max(t+1,2)
                    sol=max(sol,t)
                else:
                    break
        return sol
