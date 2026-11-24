from collections import defaultdict
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        prev_num = {}
        for i,n in enumerate(nums):
            diff = target - n
            if diff in prev_num:
                return [prev_num[diff],i]
            else:
                prev_num[n] = i
                #This is adding the num as a key and i as a value

        