class Solution:
    def areAlmostEqual(self, s1: str, s2: str) -> bool:
        if s1==s2:
            return True
        for i in s1:
            if i not in s2:
                return False
        n=[]
        for i in range(len(s1)):
            if s1[i]!=s2[i]:
                n.append(s2[i])
        if len(n)==2:
            return True
        else:
            return False