class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        repeat = []
        for num in nums:
            if num in repeat:
                return True
            else:
                repeat.append(num)
        return False

        