class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        prevnums = {}

        for i, n in enumerate(nums):
            diff = target - n
            if diff in prevnums:
                return [prevnums[diff], i]   
            prevnums[n] = i 
        return Error
         
        
        