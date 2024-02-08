#https://leetcode.com/problems/sort-characters-by-frequency/description/

#I'm proud of my solution, beats 98% python solution on fisrt try only
class Solution:
    def frequencySort(self, s: str) -> str:
        d={}
        for item in s:
            if item in d:
                d[item]+=1
            else:
                d[item]=1
        d=dict(sorted(d.items(), key=lambda x: x[1], reverse=True)) #sorting on dictoinary value
        print(d)
        sol=''
        for item in d:
            sol+=item*d[item]
        return sol
        
