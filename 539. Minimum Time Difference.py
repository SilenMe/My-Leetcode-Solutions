'''started after 1.5 month of continuos salasforce development.
made 3 super dumb mistakes which takes me to 3 wrong submissions.
lession learnt 9873485382th time: consistency is the key.'''

#please optimize the code by eleminating for loops by storing min(a,b)
class Solution:
    def findMinDifference(self, timePoints: List[str]) -> int:
        timePoints.sort()
        print(timePoints)
        new=[]
        for item in timePoints:
            temp=item.split(':')
            new.append([int(temp[0]),int(temp[1])])
        print(new)
        sol=[]
        for i in range(1,len(new)):
            sol.append((new[i][0]-new[i-1][0])*60 + new[i][1]-new[i-1][1])
        sol.append((new[0][0]+24-new[i][0])*60 + new[0][1]-new[i][1])
        print(sol)
        return min(sol)
