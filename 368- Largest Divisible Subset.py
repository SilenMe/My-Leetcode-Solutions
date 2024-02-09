#https://leetcode.com/problems/largest-divisible-subset/description/
#my TLE solution
class Solution:
    def largestDivisibleSubset(self, nums: List[int]) -> List[int]:
        # nums=[1,2,4,3,9,27]
        nums.sort()
        n=len(nums)
        d={}
        d[1]=[[i] for i in nums]
        for i in range(1,n+1):
            if d[i]==[]:
                break

            sol=[]
            for j in range(0,len(d[i])):
                for item in nums:
                    if item>d[i][j][-1] and item%d[i][j][-1]==0 and d[i][j]+[item] not in sol:
                        sol.append(d[i][j]+[item])

            d[i+1]=sol
        return d[len(d)-1][0]
#accepted solution
# the thing I was cheking the factor from starting no from end. The benifit of starting from end is that at every step we get only the optimised list item, rather than getting the entire range of subset which we get if we start from 0 index
class Solution: 
    def largestDivisibleSubset(self, nums: List[int]) -> List[int]: 
        nums.sort() 
        n = len(nums) 
        dp = [[val] for val in nums] 
        res = [] 
        for i in range(n - 1, -1, -1): 
            for j in range(i + 1, n): 
                if nums[j] % nums[i] == 0 and len(dp[j]) >= len(dp[i]): 
                    dp[i] = [nums[i]] + dp[j] 
            res = dp[i] if len(dp[i]) > len(res) else res 
        return res


                
