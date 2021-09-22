class Solution:
    def createTargetArray(self, nums: List[int], index: List[int]) -> List[int]:
# With insert
        target=[]
        for n,i in zip(nums,index): 
            target.insert(i,n)
        return target
    
# Without insert

#         target = []
#         for n,i in zip(nums,index): 
#             target[i:i] = [n]
#         return target






#         target = []
#         for i in range(len(nums)):
#             if index[i] == len(target): # compare len of index and target
#                 target.append(nums[i]) # append into the target
#             else:
#                 target = target[:index[i]] + [nums[i]] + target[index[i]:]
#         return target
