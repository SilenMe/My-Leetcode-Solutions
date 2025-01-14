class Solution:
    def findThePrefixCommonArray(self, A: List[int], B: List[int]) -> List[int]:
        both=set()
        ans=[]
        for i in range(len(A)):
            both.add(A[i])
            both.add(B[i])
            ans.append(2*(1+i)-len(both))
        return ans
