class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
#         dic1 = {}
#         for  i in s:
#             if i in dic1:
#                 dic1[i] += 1
#             else:
#                 dic1[i] = 1
                
#         dic2 = {}
#         for  i in t:
#             if i in dic2:
#                 dic2[i] += 1
#             else:
#                 dic2[i] = 1
     
#         if dic1 == dic2:
#             return True
#         return False
        
        dic1 = Counter(s)
        dic2 = Counter(t)
        if dic1 == dic2:
            return True
        return False