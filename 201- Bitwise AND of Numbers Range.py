#https://leetcode.com/problems/bitwise-and-of-numbers-range/description/
class Solution:
    def rangeBitwiseAnd(self, left: int, right: int) -> int:
        i=0
        while left!=right:
            left=(left>>1)
            right=(right>>1)
            i+=1
        return (right<<i)

#better way of implementing the same logic
class Solution:
    def rangeBitwiseAnd(self, left: int, right: int) -> int:
        while left < right:
            right = right & (right-1)
        return left & right
          
        
