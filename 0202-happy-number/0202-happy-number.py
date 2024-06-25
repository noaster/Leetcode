class Solution:
    def calcSumOfSquares(self, n: int) -> int:
        number = n
        result = 0
        while True:
            digit = number % 10
            result += digit * digit
            number = number // 10
            if number <= 0:
                break
        return result
    
    def isHappy(self, n: int) -> bool:
        resultDict = dict()
        
        number = n
        while True:
            calcNum = self.calcSumOfSquares(number)
            if calcNum == 1:
                return True
            if calcNum in resultDict:
                return False
            resultDict[number] = calcNum
            #print(f"{number} -> {calcNum}")
            number = calcNum
        return True
        