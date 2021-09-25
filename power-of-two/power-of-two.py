class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        
        if n == 1:
            return True
        if n == 0:
            return False
        
        while (1):
            rem = n%2
            n = n/2
            if rem != 0:
                return False
            if n == 1 and rem == 0:
                return True