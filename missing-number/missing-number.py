class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        
        nums.sort()
        var = 0
        for i in nums:
            if i==var:
                var+=1
            else:
                return var
        return var