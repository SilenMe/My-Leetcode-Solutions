class Solution:
    def countSubarrays(self, nums: List[int], k: int) -> int:
        maxNum, countMaxNum=max(nums),0
        l=0
        res=0
        for r in range(len(nums)):
            if nums[r]==maxNum:
                countMaxNum+=1
            while countMaxNum==k:
                if nums[l]==maxNum:
                    countMaxNum-=1
                l+=1
            res+=l
        return res
