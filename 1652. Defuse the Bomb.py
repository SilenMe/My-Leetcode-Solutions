#not easy one for sure

class Solution:
    def decrypt(self, code: List[int], k: int) -> List[int]:
        mas=code*3
        ini=len(code)
        sol=[]
        s=0
        if k>0:
            for i in range(k):
                print(mas[ini + i])
                s+=mas[ini+i]
        else:
            for i in range(k,0,1):
                s+=mas[ini+i]
        for i in range(ini,2*ini):
            sol.append(s)
            if k!=0:
                s -= mas[i] * (k // abs(k))
                s += mas[i + k] * (k // abs(k))
        if k>0:
            return sol[1:]+sol[:1]
        else:
            return sol
        
