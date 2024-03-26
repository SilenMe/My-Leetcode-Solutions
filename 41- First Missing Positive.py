#this problem should be moved to medium difficulty level

class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        mini=1
        sol={}
        for item in nums:
            if item==mini:
                mini+=1
            if item>0:
                sol[item]=mini
        while True:
            if mini not in sol:
                break
            else:
                sol[mini]=mini+1
                mini=mini+1
        return mini

                
