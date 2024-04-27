#really hard one: have to see a tutorial after several attempt

class Solution:
    def findRotateSteps(self, q: str, w: str) -> int:
        y=[0]*len(q)
        for k in reversed(range(len(w))):
            o=[float('inf')]*len(q)
            for r in range(len(q)):
                for i,c in enumerate(q):
                    if c==w[k]:
                        v=min(abs(r-i),len(q)-abs(r-i))
                        o[r]=min(o[r],v+1+y[i])
            y=o
        return y[0]

