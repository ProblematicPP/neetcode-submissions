class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hashmap = defaultdict(int)
        for num in nums:
            if not hashmap[num]:
                hashmap[num] = 1
            else:
                hashmap[num] += 1
        sorted_data = dict(sorted(hashmap.items(), key=lambda item: item[1],reverse = True))
        count = 0
        ans = []
        for key in sorted_data.keys():
            count+=1
            if count<=k:
                ans.append(key)
        return ans




        