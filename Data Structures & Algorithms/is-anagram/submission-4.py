from collections import defaultdict
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if not len(s) == len(t):
            return False
        dict_s = defaultdict(int)
        dict_t = defaultdict(int)
        for i in list(s):
            if not dict_s[i]:
                dict_s[i] = 1
            else: dict_s[i] += 1
        for i in list(t):
            if not dict_t[i]:
                dict_t[i] = 1
            else: dict_t[i] += 1
        return dict_s == dict_t

        
        