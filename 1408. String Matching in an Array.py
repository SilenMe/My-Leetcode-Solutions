#brute force sol. this brute force solution can be optimised by bucket sort for lenght of string, then arranging in list with increasing order of length
#visit KMP or Robin Karp in case you get the question with tighter contrains
class Solution:
    def stringMatching(self, words: List[str]) -> List[str]:
        sol=[]
        for i in range(len(words)):
            for j in range(0,len(words)):
                if words[i] in words[j] and i!=j:
                    sol.append(words[i])
                    break
        return sol
