class Solution:
    def longestCommonPrefix(self, arr1: List[int], arr2: List[int]) -> int:
        if len(arr2)>len(arr1):
            arr1,arr2=arr1,arr2
        mainSet=set()
        for n in arr1:
            while n:
                mainSet.add(n)
                n=n // 10
        ans=0
        for n in arr2:
            while n and n not in mainSet:
                n=n//10
            if n in mainSet:
                ans=max(ans,len(str(n)))
        return ans
        
