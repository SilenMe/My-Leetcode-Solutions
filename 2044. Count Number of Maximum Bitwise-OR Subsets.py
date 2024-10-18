class Solution:
    def countMaxOrSubsets(self, nums: List[int]) -> int:
        sm=0
        for i in nums:
            sm|=i
        def dfs(i,cur):
            nonlocal sm
            if i==len(nums):
                return 1 if cur==sm else 0
            return (
                dfs(i+1,cur)+dfs(i+1,cur|nums[i])
            )
        return dfs(0,0)
