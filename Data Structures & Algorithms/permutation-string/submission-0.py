class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        idx1 = [0]*26
        idx2 = [0]*26
        for r in range(len(s1)):
            idx1[ord(s1[r])-ord('a')] += 1
            idx2[ord(s2[r])-ord('a')] += 1
        if idx1 == idx2:
            return True
        for r in range(len(s1), len(s2)):
            idx2[ord(s2[r])-ord('a')] += 1
            idx2[ord(s2[r-len(s1)])-ord('a')] -= 1
            if idx1 == idx2:
                return True
        return False
            


        