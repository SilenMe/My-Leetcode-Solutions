#TLE solution, I optilized it little bit but that was TLE too, so now have to think about different data structure to solve the problem
class Solution:
    def minGroups(self, intervals: List[List[int]]) -> int:        
        intervals.sort()
        sol=0
        while intervals:
            toPop = []
            for i in range(1,len(intervals)):
                if intervals[0][1]<intervals[i][0]:
                    toPop.append(i)
                    intervals[0]=intervals[i]
            for i in reversed(toPop):
                intervals.pop(i)
            intervals.pop(0)
            sol+=1
        return sol

#so this is the classical tricky leetcode problem, solving it by couting the number of line at point 1/2/3/4. the maximum number of intersecting line is the answer
class Solution:
    def minGroups(self, intervals: List[List[int]]) -> int:
        start,end=[],[]
        for l,r in intervals:
            start.append(l)
            end.append(r)
        start.sort()
        end.sort()
        i,j=0,0
        res=0
        while i<len(intervals):
            if start[i]<=end[j]:
                i+=1
            else:
                j+=1
            res=max(res,i-j)
        return res
