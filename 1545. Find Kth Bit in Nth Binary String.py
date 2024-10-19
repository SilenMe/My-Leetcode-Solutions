class Solution:
    def findKthBit(self, n: int, k: int) -> str:
        l=2**n-1
        def reduce(lth,k):
            if lth==1:
                return '0'
            mid=lth//2
            if k<=mid:
                return reduce(mid,k)
            elif k>mid+1:
                res=reduce(mid,1+lth-k)
                return '0' if res=='1' else '1'
            else:
                return '1'
        return reduce(l,k)
