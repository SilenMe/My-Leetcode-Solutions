#https://leetcode.com/problems/group-anagrams/description/
#best case solution


# f = open('user.out', 'w')


# for q in map(loads, stdin):
#     w = defaultdict(list)
#     for s in q:
#         w[''.join(sorted(s))].append(s)
    
#     print(str(w.values())[12:-1].replace("'", '"').replace(" ", ""), file=f)
# exit()


#my solution
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        strscopy=['' for i in range(len(strs))]
        for i in range(len(strs)):
            strscopy[i]=''.join(sorted(strs[i])) #nlogn
        # print(strs)
        strsset=set(strscopy)
        d={}
        for item in strsset:
            for i in range(len(strscopy)):
                if(item==strscopy[i]):
                    if item in d:
                        d[item]+=[i]
                    else:
                        d[item]=[i]
        # print(d)
        sol=[]
        for item in strsset:
            insert1=[]
            for values1 in d[item]:
                insert1.append(strs[values1])
            sol.append(insert1)
        return sol
        
