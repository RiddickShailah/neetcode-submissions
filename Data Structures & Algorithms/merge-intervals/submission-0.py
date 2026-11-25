class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key=lambda i : i[0])
        output = [intervals[0]]

        for start_i, end_i in intervals[1:]:
            lastEnd = output[-1][1]
            if start_i <= lastEnd:
                output[-1][1] = max(lastEnd,end_i)
            else:
                output.append([start_i,end_i])
        return output
