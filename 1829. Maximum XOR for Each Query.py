class Solution:
    def getMaximumXor(self, nums: List[int], maximumBit: int) -> List[int]:
        xor=0
        for n in nums:
            xor^=n
        ans=[]
        mask=(1<<maximumBit)-1            #(2 power n) -1
        for n in reversed(nums):
            ans.append(xor^mask) 
            xor^=n                        #xor with self cancels out, so we get xor on nums array for each length
        return ans
