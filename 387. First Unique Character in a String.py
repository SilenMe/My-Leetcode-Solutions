#https://leetcode.com/problems/first-unique-character-in-a-string/description/
class Solution:
    def firstUniqChar(self, s: str) -> int:
        
        for i in range(len(s)):
            found=False

            #running loop from 0-i and i+1-n to find the duplicate
            for j in range(i+1,len(s)):
                if(s[i]==s[j]):
                    found=True
                    break
            for j in range(0,i): 
                if(s[i]==s[j]):
                    found=True
                    break
            #if flag is false from for an iteration of i then returning the i
            if(found==False):
                return i
        return -1
        
