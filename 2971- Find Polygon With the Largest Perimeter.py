#https://leetcode.com/problems/find-polygon-with-the-largest-perimeter/description/
class Solution:
    def largestPerimeter(self, nums: List[int]) -> int:
        nums.sort()
        for i in range(len(nums)-1,0,-1):
            if sum(nums[0:i])>nums[i]:
                return sum(nums[0:i])+nums[i]
               
        return -1

#optimized without sorting
class Solution:
    def largestPerimeter(self, nums: List[int]) -> int:
        while 1:
            if not nums: return -1
            maxx = max(nums)
            suma = sum(nums) - maxx
            if suma<=maxx: nums.remove(maxx)
            else: break  
        return sum(nums)
                
        
        
