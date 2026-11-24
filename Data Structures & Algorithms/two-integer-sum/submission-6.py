class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]: 
        num_to_index = {} # val:index

        for i, n in enumerate(nums):
            complement = target - n

            if complement in num_to_index: 
                return [num_to_index[complement], i] #returns indicies 
            else: 
                num_to_index[n] = i
        return False
        