from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        anagrams = defaultdict(list)
        res = []

        for s in strs:
            sorted_s = tuple(sorted(s))
            anagrams[sorted_s].append(s)

        for value in anagrams.values():
            res.append(value)
        
        return res
        