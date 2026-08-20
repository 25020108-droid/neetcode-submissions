class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        group_anagrams = {}
        ord_a = ord('a')
        for str in strs:
            idx_count = [0]*26
            for ch in str:
                count = ord(ch) - ord_a
                idx_count[count] += 1
            key = tuple(idx_count)
            if key not in group_anagrams:
               group_anagrams[key] = []
            group_anagrams[key].append(str)
        return list(group_anagrams.values())



