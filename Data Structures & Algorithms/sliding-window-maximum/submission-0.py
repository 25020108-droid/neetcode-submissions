class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        from collections import deque
        res = []
        d = deque() 
        for i, num in enumerate(nums):
            while d and nums[d[-1]] <= num:
                d.pop()
            d.append(i)
            if d[0] == i - k:
                d.popleft()
            if i >= k - 1:
                res.append(nums[d[0]])
        return res
        