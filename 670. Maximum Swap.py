#at first this looks easiest one then monsterous test cases started appearing one by one and we got the big picture
class Solution:
    def maximumSwap(self, num: int) -> int:
        s=str(num)
        l=[]
        dum=[]
        for item in s:
            l.append(int(item))
        while (True and l):
            mx=max(l)
            if l[0]==mx:
                l=l[1:]
                dum.append(mx)
            else:
                break
        for i in range(len(l)-1,-1,-1):
            if l[i]==mx:
                l[i]=l[0]
                l[0]=mx
        sol=0
        for item in dum:
            sol=(10*sol)+item
        for item in l:
            sol=(10*sol)+item
        return sol


        
