class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        def powerset(nums):
            if len(nums)==0:
                return [[]]
            sol=[]
            first=nums[0]
            remain=nums[1:]
            for item in powerset(remain):
                sol.append(item)
                sol.append([first]+item)
            return sol
        return powerset(nums)


        
