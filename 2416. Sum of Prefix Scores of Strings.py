#after a really long time I'm able to solve a leetcode hard problem without a single Googling: all thanks to yersterday daily problem
#the code is not really efficient, trying a different approach
class Solution:
    def sumPrefixScores(self, words: List[str]) -> List[int]:
        mainSet={}
        sol=[]
        for item in words:
            for i in range(1,len(item)+1):
                if item[0:i] in mainSet:
                    mainSet[item[0:i]]+=1
                else:
                    mainSet[item[0:i]]=1
        for item in words:
            temp = []
            count=0
            for i in range(1,len(item)+1):
                temp.append(item[0:i])
            for st in temp:
                count+=mainSet[st]
            sol.append(count)
        return sol
