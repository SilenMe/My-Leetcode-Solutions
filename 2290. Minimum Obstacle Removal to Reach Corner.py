#problem is a variation of dijkstra algorithm
class Solution:
    def minimumObstacles(self, grid: List[List[int]]) -> int:
        rows,cols=len(grid),len(grid[0])
        q=deque([(0,0,0)]) #(obstacle,rowPointer,colPointer)
        visited=set([(0,0)]) #(row,col)
        while q:
            obstacle,r,c=q.popleft()
            if (r,c)==(rows-1,cols-1):
                return obstacle
            nxt=[[r+1,c],[r-1,c],[r,c+1],[r,c-1]]
            for nxtRow,nxtCol in nxt:
                if (nxtRow,nxtCol) in visited or nxtRow<0 or nxtCol<0 or nxtRow==rows or nxtCol==cols:
                    continue
                if grid[nxtRow][nxtCol]: #if 1
                    q.append((obstacle+1,nxtRow,nxtCol))
                else:
                    q.appendleft((obstacle,nxtRow,nxtCol))
                visited.add((nxtRow,nxtCol))
