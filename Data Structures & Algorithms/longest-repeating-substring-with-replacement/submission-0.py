class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l = 0 
        hash = {}
        max_freq = 0
        max_len = 0
        for r in range(len(s)):
            char = s[r]
            hash[char] = hash.get(char, 0) + 1
            freq = hash[char]
            max_freq = max(freq, max_freq)
            conditions = r - l + 1 - max_freq 
            if conditions > k:
               hash[s[l]] -= 1
               l += 1
            max_len = max(max_len, r - l + 1)
        return max_len
        