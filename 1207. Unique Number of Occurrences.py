# https://leetcode.com/problems/unique-number-of-occurrences/description/
class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        d={}
        for item in arr:
            if item in d:
                d[item]+=1
            else:
                d[item]=1
        freq=[]
        for item in d:
            freq.append(d[item])

        for i in range(len(freq)-1):
            for j in range(i+1,len(freq)):
                if freq[i]==freq[j]:
                    return False
            
        return True
