#uff the edge cases, I lost my accuracy points
class Solution:
  def canChange(self,start:str,target:str)->bool:
    n=len(start)
    i=0
    j=0
    while i<=n and j<=n:
      while i<n and start[i]=='_':
        i+=1
      while j<n and target[j]=='_':
        j+=1
      if i==n or j==n:
        return i==n and j==n
      if start[i]!=target[j]:
        return False
      if start[i]=='R' and i>j:
        return False
      if start[i]=='L' and i<j:
        return False
      i+=1
      j+=1
    return True