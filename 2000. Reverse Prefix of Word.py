class Solution:
    def reversePrefix(self, word: str, ch: str) -> str:
        fast=-1
        sol=''
        for i in range(len(word)):
            if ch==word[i]:
                fast=i
                break
        if fast!=-1:
            for i in range(fast,-1,-1):
                sol+=word[i]
            if fast!=len(word):
                sol+=word[fast+1:]
        else:
            sol=word
        return sol

#a better way of same logic
class Solution:
    def reversePrefix(self, word: str, ch: str) -> str:
        x=0
        for i in range(len(word)):
            if word[x]==ch:
                return word[x::-1]+word[x+1:]
            x+=1
        return word
