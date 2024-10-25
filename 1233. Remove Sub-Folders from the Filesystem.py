#my solution
class Solution:
    def removeSubfolders(self, folder: List[str]) -> List[str]:
        folder.sort()
        sol=[]
        track=0
        trie={}
        for item in folder:
            trieIter=trie
            tempList=item.split('/')[1:]
            broke=False
            for i in range(len(tempList)):
                if tempList[i] not in trieIter:
                    if i==len(tempList)-1:
                        trieIter[tempList[i]]={2}
                    else:
                        trieIter[tempList[i]] = {}
                    trieIter = trieIter[tempList[i]]
                else:
                    trieIter = trieIter[tempList[i]]
                    if 2 in trieIter:
                        broke=True
                        break
            if not broke:
                sol.append(folder[track])
            track+=1
        return sol




#optimized solution, I'm a noob that why this struck after watching the hint:
class Solution:
    def removeSubfolders(self, folder: List[str]) -> List[str]:
        folder.sort()  
        result = []
        prev = ''
        for path in folder:
            if not prev or not path.startswith(prev + '/'):
                result.append(path)
                prev = path  # Update 'prev' to the current folder
        return result
