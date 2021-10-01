class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        
        s_arr = set(nums)
        ans = []
        for i in range(len(nums)):
            if i+1 not in s_arr:
                ans.append(i+1)
        return ans
    
        # expect = set()
        # for i in range(1,len(nums)+1):
        #     expect.add(i)    
        # actual = set(nums)
        # return list(expect-actual)