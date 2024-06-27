class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        #Approach : Sorting
        intervals.sort(key=lambda x: x[0])

        mergedIntervals = []
        for interval in intervals:
            if not mergedIntervals or mergedIntervals[-1][1] < interval[0]:
                mergedIntervals.append(interval)
            else:
                mergedIntervals[-1][1] = interval[1] if interval[1] >= mergedIntervals[-1][1] else mergedIntervals[-1][1]
        
        return mergedIntervals