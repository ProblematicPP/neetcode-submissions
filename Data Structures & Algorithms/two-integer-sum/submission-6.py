class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
      mapped = {}
      for i , v in enumerate(nums):
        rem = target - v
        if rem in mapped:
            return [mapped[rem],i]
        mapped[v] = i
        