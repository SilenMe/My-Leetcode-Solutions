class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        main={}
        main2={}
        for i in range(len(s)):
            if s[i] in main:
                if main[s[i]]!=t[i]:
                    return False
            else:
                main[s[i]]=t[i]
        for i in range(len(s)):
            if t[i] in main2:
                if main2[t[i]]!=s[i]:
                    return False
            else:
                main2[t[i]]=s[i]
        return True
        
