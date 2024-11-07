class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        def getAllSubsets(nums):
            if len(nums)==0:
                return [[]]
            solList=[]
            startingPart=nums[0]
            endingPart=nums[1:]
            for item in getAllSubsets(endingPart):
                solList.append(item)
                solList.append([startingPart]+item)
            return solList
        xorVal=0
        allSubsets=getAllSubsets(nums)[1:]
        for listItems in allSubsets:
            tempXor=0
            for item in listItems:
                tempXor^=item
            xorVal+=tempXor
        return xorVal
