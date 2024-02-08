#https://leetcode.com/problems/perfect-squares/description/

#im proud of my sol as its my fisrt DP-Medium sol in first attempt + without a single google/chatgpt search
#use Langrage's 4 Square theorem for more optimised solution as suggeted by some brillient folks
import math
class Solution:
    def numSquares(self, n: int) -> int:
        # writing comments for n=12
        maxsqrt=int(math.sqrt(n)) #3
        reqlist=[]
        sollist=[10001 for i in range(n+1)] #[10001 for n+1 times]
        for i in range(1,maxsqrt+1):
            reqlist.append(i*i) #reqlist=[1,4,9]
        for item in reqlist:
            sollist[item]=1 #1 at perfect square index [10001,1,10001,10001,1,10001,10001,10001,10001,10001,1]
        for i in range(2,n+1):
            lll=[]
            for item in reqlist:
                if (i-item)>0:
                    lll.append(min(sollist[i - item]+sollist[item],sollist[i])) #min(exsting, 12-1,12-4,12-9th index)

            sollist[i]=min(lll) #placing the minimum at ith index
        return sollist[n] #returning the ith index


