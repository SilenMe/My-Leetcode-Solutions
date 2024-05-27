#not an easy question, the optimal solution need a lot of thiking
class Solution(object):
    def specialArray(self,m):
        lim=1000
        c=[0]*(lim+1)
        for p in m:
            c[p]+=1
        n=len(m)
        for i in range(len(c)):
            if i==n:
                return i
            n-=c[i]
        return -1
