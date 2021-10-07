class Solution:
    def sortSentence(self, s: str) -> str:                  
        lst = s.split()
        lst2=lst.copy()
        
        for i in range(len(lst)):
            idx = ord(lst[i][-1])-49
            lst2[idx] = lst[i][:-1]

        return " ".join(lst2)