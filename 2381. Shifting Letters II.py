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

#optimized it by using prefix-sum technique, This was the really tricky part
class Solution:
    def shiftingLetters(self, s: str, shifts: List[List[int]]) -> str:
        indx = [0] * (len(s) + 1)
        for a, b, d in shifts:
            indx[b + 1] += 1 if d else -1
            indx[a] += -1 if d else 1
        diff = 0
        res = [ord(c) - ord("a") for c in s]
        for i in reversed(range(len(indx))):
            diff += indx[i]
            res[i - 1] = (diff + res[i - 1] + 26) % 26
        s = [chr(ord("a") + n) for n in res]
        return "".join(s)
