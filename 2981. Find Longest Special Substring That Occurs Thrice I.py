#contrains made problem easy
from collections import Counter
class Solution:
    def maximumLength(self,s:str)->int:
        combo=[] #making combo of substrs
        for i in range(len(s)):
            lft=i
            while lft<len(s) and s[lft]==s[i]:
                combo.append(s[i:lft+1])
                lft+=1
        freq=Counter(combo)
        ans=0
        for j,n in freq.items():
            if n>=3:
                if len(j)>ans:
                    ans=len(j)
        if ans==0:
            return -1            
        return ans
