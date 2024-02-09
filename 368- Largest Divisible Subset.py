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
        


                
