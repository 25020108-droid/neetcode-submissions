import math
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        piles.sort()
        n = len(piles)
        m = max(piles)
        l = 1
        ans = m
        while l <= m:
            rate = (l+m) // 2
            total = 0
            for p in piles:
                total += math.ceil(p / rate)
            if total <= h:
                ans = min(rate,ans)
                m = rate - 1
            else:
                l = rate + 1
        return ans
                

