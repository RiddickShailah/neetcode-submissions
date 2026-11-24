class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        #STEPS:
        #1. Make a list of numbers already seen (nums_seen)
        #2. Loop through nums
        #3. If n in nums is in nums_seen then return true
        #4. If it isnt then add n to nums_seen
        #5. Anything else is false
        nums_seen = set()
        for n in nums:
            if n in nums_seen:
                return True
            else:
                 nums_seen.add(n)
        return False
        
            