class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        length = len(nums) - 1
        for a in range(length):
            for b in range(a + 1, length + 1):
                if nums[a] + nums[b] == target:
                    return [a, b]
