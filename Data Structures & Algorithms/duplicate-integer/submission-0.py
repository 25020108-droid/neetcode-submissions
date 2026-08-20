class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        container = set()
        for num in nums:
            if num in container:
                return True
            else:
                container.add(num)
        return False
