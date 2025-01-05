#TLE   we can optimize the code from line 6 to 11: finding a way to do that because rest code is well optimized
class Solution:
    def shiftingLetters(self, s: str, shifts: List[List[int]]) -> str:
        indx=[0 for _ in range(len(s))]
        sol=''
        for a,b,c in shifts:
            for j in range(a,b+1):
                if c==0:
                    indx[j]-=1
                else:
                    indx[j]+=1
        for i in range(len(indx)):
            ordAdd=(26+indx[i])%26
            ordFin=(ord(s[i])-97+ordAdd)%26
            sol+=chr(97+ordFin)
        return sol
