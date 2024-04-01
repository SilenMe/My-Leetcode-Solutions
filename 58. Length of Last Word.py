class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        spaces=0
        seenNonSpace=False
        for i in range(len(s)-1,-1,-1):
            if s[i]==' ' and seenNonSpace:
                return len(s)-i-spaces-1
            if s[i]==' ':
                spaces+=1
            else:
                seenNonSpace=True
        return len(s)-spaces
        
