class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        sum = 0
        a = []
        for i in nums:
            sum += i
            a.append(sum)
        return a