class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        count = {}
        for i,a in enumerate(nums):
            count[a] = i

        for i in nums:
            if target - i in count and count[target - i] != nums.index(i):
                return [nums.index(i), count[target - i]]
        