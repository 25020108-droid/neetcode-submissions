class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        prev_num = {}
        for idx, num in enumerate(nums):
            adder = target - num
            if adder in prev_num:
                return [prev_num[adder], idx]
            prev_num[num] = idx
