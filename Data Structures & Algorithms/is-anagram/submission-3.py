class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        count_s = {}
        count_t = {}
        for ch in s:
            count_s[ch] = count_s.get(ch, 0) +1
        for cha in t:
            count_t[cha] = count_t.get(cha, 0) +1
        if count_s == count_t:
            return True
        else:
            return False
        