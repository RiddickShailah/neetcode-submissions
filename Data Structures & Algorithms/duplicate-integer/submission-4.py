class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        #make a empty set
        #add any numbers already seen to the set
        #if the number is already in the already seen set then return True
        #else: return false
        seen = set()
        for n in nums:
            if n in seen:
                return True
            else:
                seen.add(n)
        return False
