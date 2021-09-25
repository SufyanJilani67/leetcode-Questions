class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        # dic = Counter(nums) 
        
        dic = {}
        for i in nums:
            if i in dic:
                dic[i] += 1
            else:
                dic[i] = 1
                
        n = len(nums)//2
        for i in nums:
            if dic[i] > n:
                return i