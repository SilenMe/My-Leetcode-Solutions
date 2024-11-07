#my intution is: count the number of bits at each decimal point,the answer will be the unit count on which the the count of 1 is max
class Solution:
    def largestCombination(self, candidates: List[int]) -> int:
        onesFreq={}
        for item in candidates:
            it=bin(item)[2:][::-1] #reversing the string so that unit, decimal, hundred... places matches for each postion
            for i in range(len(it)):
                if it[i]=='1':
                    if i in onesFreq:
                        onesFreq[i]+=1
                    else:
                        onesFreq[i]=1
        sol=0
        for item in onesFreq:
            sol=max(sol,onesFreq[item])
        return sol


#bitwise sol, counting the frequency at i'th decimal place and max is ans
class Solution:
    def largestCombination(self, candidates: List[int]) -> int:
        ans=0
        for i in range(32):
            iCount=0
            for n in candidates:
                iCount+=1 if (1<<i) & n else 0
            ans=max(ans,iCount)
        return ans
