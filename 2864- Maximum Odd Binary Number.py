#https://leetcode.com/problems/maximum-odd-binary-number/description
class Solution:
    def maximumOddBinaryNumber(self, s: str) -> str:
        l=len(s)
        sol=[0]*l
        place=0
        for item in s:
            if item=='1':
                if sol[-1]!=1:
                    sol[-1 ]= 1
                else:
                    sol[place]=1
                    place+=1
        ss=''
        for item in sol:
            ss+=str(item)
        return ss


class Solution:
    def maximumOddBinaryNumber(self, s: str) -> str:
        ones = s.count('1')
        return ('1' * (ones - 1)) + ('0' * (len(s) - ones)) + '1'
