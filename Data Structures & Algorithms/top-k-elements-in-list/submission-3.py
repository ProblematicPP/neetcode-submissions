class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hashmap = defaultdict(int)
        for num in nums:
            if not hashmap[num]:
                hashmap[num] = 1
            else:
                hashmap[num] += 1
        sorted_data = dict(sorted(hashmap.items(), key=lambda item: item[1],reverse = True))
        return list(sorted_data.keys())[:k]




        