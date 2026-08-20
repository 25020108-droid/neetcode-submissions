class Solution:

    def encode(self, strs: List[str]) -> str:
        s = ""
        for chr in strs:
            en_chr = str(len(chr)) + '%' + chr
            s += en_chr
        return s

    def decode(self, s: str) -> List[str]:
        res = []
        i = 0
        while i < len(s):
            j = i
            while s[j] != '%':
                j = j + 1
            length = int(s[i:j])
            i = j + 1
            j = i + length
            res.append(s[i:j])
            i = j
        return res

        

        
