class Solution:
    def highestPeak(self, isWater: List[List[int]]) -> List[List[int]]:
        R,C=len(isWater),len(isWater[0])
        q=deque()
        res=[[-1]*C for _ in range(R)]
        for r in range(R):
            for c in range(C):
                if isWater[r][c]:
                    q.append((r,c)) #multi source BFS
                    res[r][c]=0
        while q:
            r,c=q.popleft()
            curHeight=res[r][c]
            nei=[[r-1,c],[r+1,c],[r,c-1],[r,c+1]]
            for nr,nc in nei:
                if nr>-1 and nc>-1 and nr<R and nc<C and res[nr][nc]==-1:
                    q.append((nr,nc))
                    res[nr][nc]=curHeight+1
        return res
