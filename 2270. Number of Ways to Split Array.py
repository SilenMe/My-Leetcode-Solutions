#I wish if I get this medium level in the interview
class Solution:
    def waysToSplitArray(self, nums: List[int]) -> int:
        left=0
        right=sum(nums)
        sol=0
        for i in range(len(nums)-1):
            left+=nums[i]
            right-=nums[i]
            if left>=right:
                sol+=1
        return sol
