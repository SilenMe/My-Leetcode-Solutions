class Solution:
    def canMakeSubsequence(self,str1:str,str2:str) -> bool:
        str2Index=0
        for c in str1:
            if c== 'z':
                nxtC='a' 
            else:
                nxtC=chr(ord(c)+1)
            if str2Index<len(str2):
                if str2[str2Index] in (c,nxtC): #either char c or c+1 th char
                    str2Index += 1
        return str2Index==len(str2)
