class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        n = set(nums)
        if len(n) < 3:
            return max(n)
        elif len(n) == 3:
            return min(n)
        else:
            ref = -2**31
            for i in n:
                if i > ref:
                    ref = i
            n.remove(ref)
            m2 = max(n)
            n.remove(m2)
            return max(n)