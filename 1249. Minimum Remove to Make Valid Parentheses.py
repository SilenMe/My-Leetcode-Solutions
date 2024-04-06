class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        count=0
        sol=[]
        for item in s:
            if item=='(':
                count+=1
                sol.append(item)
            elif item==")" and count!=0:
                sol.append(item)
                count-=1
            elif item==")" and count==0:
                pass
            else:
                sol.append(item)
        print(sol)

        for i in range(len(sol)-1,-1,-1):
            if count>0 and sol[i]=='(':
                sol[i]=''
                count-=1
        mainsol=''
        for item in sol:
            mainsol+=item
        return mainsol

        
