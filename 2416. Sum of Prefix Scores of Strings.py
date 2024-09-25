#after a really long time I'm able to solve a leetcode hard problem without a single Googling: all thanks to yersterday daily problem
#the code is not really efficient, trying a different approach
class Solution:
    def sumPrefixScores(self,k:List[str])->List[int]:
        M={}
        q=[]
        for y in k:
            for i in range(1,len(y)+1):
                if y[0:i] in M:
                    M[y[0:i]]+=1
                else:
                    M[y[0:i]]=1
        for y in k:
            r=[]
            z=0
            for i in range(1,len(y)+1):
                r.append(y[0:i])
            for st in r:
                z+=M[st]
            q.append(z)
        return q
