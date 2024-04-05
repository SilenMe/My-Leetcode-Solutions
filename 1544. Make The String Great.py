class Solution:
    def makeGood(self, s: str) -> str:
        
        found=True
        while found:
            if len(s)==1:
                return s
            for i in range(len(s)-1):
                if i == len(s) - 2:
                    found = False
                if abs(ord(s[i])-ord(s[i+1]))==32:
                    s=s[:i]+s[i+2:]
                    break

        return s
        
