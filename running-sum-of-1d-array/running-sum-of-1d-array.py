class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
# Method 1
        sum = 0
        a = []
        for i in nums:
            sum = i + sum
            a.append(sum)
        return(a)