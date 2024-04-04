class Solution:
    def maxDepth(self, s: str) -> int:
        count=0
        maxcount=0
        for item in s:
            if item=='(':
                count+=1
                if count>maxcount:
                    maxcount=count
            if item==')':
                count-=1
            
        return maxcount
        
