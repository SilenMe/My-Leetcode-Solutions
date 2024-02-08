#https://leetcode.com/problems/set-mismatch/description/?envType=daily-question&envId=2024-01-22
class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        n=len(nums)
        freq=[0 for i in range(n+1)]
        dob=non=-1
        for item in nums:
            freq[item]+=1
        for i in range(n+1):
            if(freq[i]==2):
                dob=i
            if(freq[i]==0):
                non=i
        return [dob,non]
