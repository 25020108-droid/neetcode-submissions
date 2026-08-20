class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(s) < len(t):
            return ""
        map_T = {}
        for char in t:
            map_T[char] = map_T.get(char, 0) + 1

        required_count = 0
        for _ in map_T:
           required_count += 1
    
        l = 0
        current_window = {}
        formed_count = 0
        min_len = float('inf')
        
        for r in range(len(s)):
            current_char = s[r]
            if current_char in map_T:
                current_window[current_char] = current_window.get(current_char, 0) + 1
                if current_window[current_char] == map_T[current_char]:
                   formed_count += 1
            while formed_count == required_count:
                current_len = r - l + 1
                if current_len < min_len:
                   min_len = current_len
                   min_start = l
                d = s[l]
                if d in map_T:
                    if current_window[d] == map_T[d]:
                       formed_count -= 1
                    current_window[d] -= 1
                l += 1
        if min_len == float('inf'):
           return ""
        else:
           return s[min_start : min_start + min_len]
