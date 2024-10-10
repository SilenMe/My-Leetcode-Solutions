class Solution:
    def maxWidthRamp(self, nums: List[int]) -> int:
        maxR=[0]*len(nums)  #store max value in the right array from index i
        i=len(nums)-1
        prevMax=0
        for n in reversed(nums):
            maxR[i]=max(n,prevMax)
            prevMax=maxR[i]
            i-=1
        res=0
        l=0
        for r in range(len(nums)):
            while nums[l]>maxR[r]:
                l+=1
            res=max(res,r-l)
        return res

        
