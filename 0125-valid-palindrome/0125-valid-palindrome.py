class Solution:
    def nextIndex(self, s: str, i: int, dir: int, max: int) -> int:
        while s[i] < '0' or (s[i] > '9' and s[i] < 'A') or (s[i] > 'Z' and s[i] < 'a') or s[i] > 'z':
            i = i + dir
            if i > max or i < 0:
                break
            
        return i
    
    def isPalindrome(self, s: str) -> bool:
        length = len(s)
        if length <= 1:
            return True
        
        maxIndex = length - 1
        begin = self.nextIndex(s, 0, 1, maxIndex);
        end = self.nextIndex(s, maxIndex, -1, maxIndex);
        
        if (begin > maxIndex) and (end < 0):
            return True
        if (begin > maxIndex) or (end < 0):
            return False

        while begin < end:
            beginChar = ord(s[begin])
            endChar = ord(s[end])
                        
            if beginChar != endChar and (s[begin] < 'A' or s[end] < 'A' or (abs(beginChar - endChar) != 32)):
                return False
            
            begin = self.nextIndex(s, begin + 1, 1, length - 1);
            end = self.nextIndex(s, end - 1, -1, length - 1);
            
        return True;
