class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        if len(nums) == 1:

            return nums

        if len(nums) == 0:

            return []

        n = len(nums)

        res = []

        for l in range(n-k+1):

            current_max = float('-inf')

            r = l + k - 1

            for i in range(l,r+1):

                current_max = max(current_max, nums[i])

            res.append(current_max)

        return res
        