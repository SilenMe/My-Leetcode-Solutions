#https://leetcode.com/problems/rearrange-array-elements-by-sign/description/
class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        pos=[]
        neg=[]
        for item in nums:
            if item>=0:
                pos.append(item)
            else:
                neg.append(item)
        for i in range(len(pos)):
            nums[2*i]=pos[i]
            nums[2*i+1]=neg[i]
        return nums

#two pointer solution
class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        ans = [0] * len(nums)
        pos, neg = 0, 1
        
        for num in nums:
            if num > 0:
                ans[pos] = num
                pos += 2
            else:
                ans[neg] = num
                neg += 2
        
        return ans

