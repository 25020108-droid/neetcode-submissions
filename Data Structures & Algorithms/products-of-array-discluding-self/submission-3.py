class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        ans = []
        for i in range(len(nums)):
            current_num = nums[i]
            productor = 1
            for j in range(len(nums)):
                if i != j:
                    productor *= nums[j]
            ans.append(productor)
        return ans
