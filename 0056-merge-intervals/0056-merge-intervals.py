class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        result = [intervals[0]]
        
        lengthOfIntervals = len(intervals)
        for i in range(lengthOfIntervals - 1):
            target = intervals[i + 1]

            lengthOfResult = len(result)
            insertIdx = len(result) - 1
            mergedIdx = -1
            #print(f"{target} / {result[0][0]} {result[lengthOfResult-1][1]} / result {result}")
            for j in range(len(result)):
                if result[j][0] == -1:
                    continue
                if (target[0] < result[j][0] and target[1] < result[j][0]):
                    insertIdx = j if j < insertIdx else insertIdx
                    continue
                if (target[0] > result[j][1] and target[1] > result[j][1]):
                    insertIdx = j + 1 if j + 1 > insertIdx else insertIdx
                    continue
                    
                if mergedIdx != -1 :
                    result[mergedIdx][0] = min(result[j][0], result[j][1], result[mergedIdx][0])
                    result[mergedIdx][1] = max(result[j][0], result[j][1], result[mergedIdx][1])
                    result[j][0] = -1
                    result[j][1] = -1
                else:
                    result[j][0] = min(target[0], target[1], result[j][0])
                    result[j][1] = max(target[0], target[1], result[j][1])
                    mergedIdx = j
            
            if mergedIdx == -1:
                result.insert(insertIdx, target)
                
        result = [element for element in result if element[0] != -1]
        return result