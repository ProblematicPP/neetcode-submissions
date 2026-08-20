class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if nums == [] : return 0
        numss = set(nums)
        print(numss)
        values = []
        counter = 1
        for key in numss:
            if key-1 not in numss:
                while key+1 in numss:
                    counter+=1
                    key+=1
                values.append(counter)
            else:
                counter = 1
                continue
        return max(values)


