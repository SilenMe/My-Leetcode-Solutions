#trie solution: easy one
class Solution:
    def longestCommonPrefix(self, arr1: List[int], arr2: List[int]) -> int:
        trie={}
        for n in arr1:
            n=str(n)
            temp=trie
            for item in n:
                if item not in temp:
                    temp[item]={}
                temp = temp[item]
        sol=0
        for item in arr2:
            temp=0
            tempTrie=trie
            item=str(item)
            for st in item:
                if st in tempTrie:
                    temp+=1
                    tempTrie=tempTrie[st]
                else:
                    break
            sol=max(temp,sol)
        return sol


        
#optimized solution after Hint1: there is not much difference in time complexity in both the solution but this one is easy to implement and only work with numbers
#if instead of number, strings are given then trie is the optimal one
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
        
