#tutorial solution after 4 wrong submission
class Solution:
    def findKthNumber(self, n: int, k: int) -> int:
        cur=1
        i=1
        def count(cur):
            res=0
            nie=cur+1
            while cur<=n:
                res+=min(nie,n+1)-cur
                cur*=10
                nie*=10
            return res
        while i<k:
            steps=count(cur)
            if i+steps<=k:
                cur+=1
                i+=steps
            else:
                cur*=10
                i+=1
        return cur
        
