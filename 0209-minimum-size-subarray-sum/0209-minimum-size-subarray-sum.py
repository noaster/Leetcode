from collections import deque
class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        #Approach: Sliding Window
        lengthOfNums = len(nums)
        if lengthOfNums == 0:
            return 0

        sumOfNums = nums[0]
        foundLevel = -1
        beginIndex = 0
        endIndex = 0
        while beginIndex < lengthOfNums and endIndex < lengthOfNums:
            #print(f"{beginIndex} {endIndex} {sumOfNums}")
            if sumOfNums >= target:
                level = endIndex - beginIndex + 1
                foundLevel = level if foundLevel == -1 or foundLevel > level else foundLevel
                
                sumOfNums -= nums[beginIndex]
                beginIndex += 1
            else:
                endIndex += 1
                sumOfNums += nums[endIndex] if endIndex < lengthOfNums else 0
        return 0 if foundLevel < 0 else foundLevel