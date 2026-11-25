class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        count = {}
        res = [] 
        freq = [[] for i in range(len(nums)+1)]

#increments and adds the count num to the number
        for n in nums:
            count[n] = 1 + count.get(n,0)
#Adds number in bucket of how many times it shows up
        for n, cnt in count.items():
            freq[cnt].append(n)
        
        for i in range(len(freq)-1, 0, -1):
            for n in freq[i]:
                res.append(n)
            if len(res) == k:
                return res
                


        

        