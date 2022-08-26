class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        merged_intervals = [intervals[0]]
        for item in intervals:
            if merged_intervals[-1][0] <= item[0] <= merged_intervals[-1][1]:
                merged_intervals[-1][1] = max(item[1], merged_intervals[-1][1])
            else:
                merged_intervals.append(item)
        return merged_intervals      