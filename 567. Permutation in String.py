class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        s1l, s2l = [0] * 26, [0] * 26
        for i in range(len(s1)):
            s1l[ord(s1[i]) - ord("a")] += 1
            s2l[ord(s2[i]) - ord("a")] += 1
        matches = 0
        for i in range(26):
            matches += 1 if s1l[i] == s2l[i] else 0
        l = 0
        for r in range(len(s1), len(s2)):
            if matches == 26:
                return True
            index = ord(s2[r]) - ord("a")
            s2l[index] += 1
            if s1l[index] == s2l[index]:
                matches += 1
            elif s1l[index] + 1 == s2l[index]:
                matches -= 1

            index = ord(s2[l]) - ord("a")
            s2l[index] -= 1
            if s1l[index] == s2l[index]:
                matches += 1
            elif s1l[index] - 1 == s2l[index]:
                matches -= 1
            l += 1
        return matches == 26
