class Solution:
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
        
        dic = {}
        for i in range(len(list1)):
            for j in range(len(list2)):
                if list1[i] == list2[j]:
                    dic[list1[i]] = i+j
                    
        c = None
        for i in dic:
            if c == None:
                c = dic[i]
            if c > dic[i]:
                c = dic[i]
                
        lst = []
        for i in dic:
            if c == dic[i]:
                lst.append(i)
        return (lst)