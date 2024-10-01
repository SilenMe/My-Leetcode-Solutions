class Solution:
    def canArrange(self, arr: List[int], k: int) -> bool:
        sol=[0]*k                       #to track the frequency of remainders
        for items in arr:
            item=items%k
            sol[item]+=1
        if sol[0]%2!=0:                  #count of remainder 0 should be even(includind 0)
            return False
        for i in range(1,len(sol)+1//2):
            if sol[i]!=sol[-i]:          #if count of k-remainder and remainder is not same return false, else sum is devisible by k
                return False
        return True

        
