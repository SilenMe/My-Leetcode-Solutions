#after a really long time I'm able to solve a leetcode hard problem without a single Googling: all thanks to yersterday daily problem
#the code is not really efficient, trying a different approach
class Solution:
    def sumPrefixScores(self, words: List[str]) -> List[int]:
        mainSet={}
        sol=[]
        for item in words:
            for i in range(1,len(item)+1):
                if item[0:i] in mainSet:
                    mainSet[item[0:i]]+=1
                else:
                    mainSet[item[0:i]]=1
        for item in words:
            temp = []
            count=0
            for i in range(1,len(item)+1):
                temp.append(item[0:i])
            for st in temp:
                count+=mainSet[st]
            sol.append(count)
        return sol


#trie solution more optimized

class PrefixNode:                  # to store nodes on trie
    def __init__(self):
        self.children=[None]*26
        self.count=0
class PrefixTree:                  #initiate a trie of node 
    def __init__(self):
        self.root=PrefixNode()
    def insert(self,w):
        cur=self.root
        for c in w:
            i=ord(c)-ord('a')
            if not cur.children[i]:
                cur.children[i]=PrefixNode()
            cur=cur.children[i]
            cur.count+=1
    def get_score(self,w):
        cur=self.root
        score=0
        for c in w:
            i=ord(c)-ord('a')
            cur=cur.children[i]
            score+=cur.count
        return score
class Solution:
    def sumPrefixScores(self,words:List[str])->List[int]:
        res=[]
        prefix_tree=PrefixTree()
        for w in words:
            prefix_tree.insert(w)
        for w in words:
            res.append(prefix_tree.get_score(w))
        return res
