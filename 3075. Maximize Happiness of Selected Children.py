class Solution:
    def maximumHappinessSum(self, happiness: List[int], k: int) -> int:
        happiness.sort()
        sol=0
        temp=0
        for i in range(len(happiness)-1,-1,-1):
            if happiness[i]-temp<1 or k==0:
                k=0
                break
            sol+=happiness[i]-temp
            temp+=1
            k-=1
        return sol
        
