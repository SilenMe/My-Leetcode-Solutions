#https://leetcode.com/problems/majority-element/description/
#this is not most optimized as its using o(n) space in hash map
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        d={}
        for item in nums:
            if item in d:
                d[item]+=1
            else:
                d[item]=1
        ans=-1
        for item in d:
            ans=max(ans,d[item])
        for item in d:
            if d[item]==ans:
                return item


#found this o(1) space complexity code on and im quite impressed with the code(boyer-moore algo)
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        res,count=0,0
        for n in nums:
            if count==0:
                res=n
            count+=(1 if n==res else -1)
        return res
        
