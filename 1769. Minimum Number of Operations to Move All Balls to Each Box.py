#there must be some way to merge code from line 6-12 and line 13-19 in one for loop but today I'm lazy to do
class Solution:
    def minOperations(self, boxes: str) -> List[int]:
        resLeft=[0 for _ in range(len(boxes))]
        resRight=[0 for _ in range(len(boxes))]
        curBalls=0
        currMoves=0
        for i in range(len(boxes)):
            currMoves=curBalls+currMoves
            resLeft[i]=currMoves
            if boxes[i]=='1':  #curBalls=int(boxes[i])
                curBalls+=1
        curBalls=0
        currMoves=0
        for i in range(len(boxes)-1,-1,-1):
            currMoves=curBalls+currMoves
            resRight[i]=currMoves
            if boxes[i]=='1':  #curBalls=int(boxes[i])
                curBalls+=1
        for i in range(len(boxes)):
            resLeft[i]+=resRight[i]
        return resLeft

        
