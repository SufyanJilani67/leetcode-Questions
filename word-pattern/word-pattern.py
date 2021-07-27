class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        spl = s.split()
        print(spl)
        if len(spl) != len(pattern):
            return False
        newDict = dict()
        length = len(spl)
        new_dict_keys = newDict.keys()
        new_dict_vals = newDict.values()
        for i in range(length):
            if pattern[i] not in new_dict_keys:
                if spl[i] in new_dict_vals:
                    return False
                newDict[pattern[i]] = spl[i]
            else:
                if newDict[pattern[i]] != spl[i]:
                    return False
        return True
       
        