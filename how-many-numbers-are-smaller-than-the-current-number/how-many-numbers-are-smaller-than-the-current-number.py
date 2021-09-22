class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        
        # arr = []
        # for i in nums:
        #     count=0
        #     for j in nums:
        #         if i > j:
        #             count+=1
        #     arr.append(count)
        # return arr 
    
        sorted_nums = sorted(nums)
        for i in range(len(nums)):
            nums[i] = sorted_nums.index(nums[i])
        return nums