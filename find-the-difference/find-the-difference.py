class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        dic1=Counter(s)
        dic2=Counter(t)
        # print(dic1)
        # print(dic2)
        for i in t:
            if dic1[i]==dic2[i]:
                continue
            else:
                return i