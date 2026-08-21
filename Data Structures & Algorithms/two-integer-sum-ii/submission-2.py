class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        left = 0
        mapped = defaultdict(int)
        for i in range(len(numbers)):
            if (target-numbers[i]) in mapped:
                return [mapped[target-numbers[i]],i+1]
            mapped[numbers[i]] = i+1
