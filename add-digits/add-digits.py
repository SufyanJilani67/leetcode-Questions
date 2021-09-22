class Solution:
    def addDigits(self, num: int) -> int:
        
        if num < 10:
            return num
        
        s = 0
        while (1):
            while num != 0:
                rem = num%10
                num = num//10
                s += rem
            if s < 10:
                return s
            else:
                num = s
                s = 0