class Solution:
    def buildArray(self, nums: List[int]) -> List[int]:
         # Method 1
        output = []
        for i in nums:
            output.append(nums[i])
        return output
    
        # Method 2 (List Comprehension)
       # return [nums[i] for i in nums]