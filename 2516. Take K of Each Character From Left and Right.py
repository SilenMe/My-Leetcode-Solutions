#think in reverse, we have to maximum window which make all frequency less than k
class Solution:
    def takeCharacters(self, s: str, k: int) -> int:
        freq=[0,0,0]
        for c in s:
            freq[ord(c)-ord('a')]+=1
        if min(freq)<k:
            return -1
        ans=float("inf")
        l=0
        for r in range(len(s)):
            freq[ord(s[r])-ord('a')]-=1
            while min(freq)<k:
                freq[ord(s[l])-ord('a')]+=1
                l+=1
            ans=min(ans,len(s)-(r-l+1))
        return ans

        
