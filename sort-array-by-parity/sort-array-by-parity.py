class Solution(object):
    def sortArrayByParity(self, A):
        """
        :type A: List[int]
        :rtype: List[int]
        """
        even = []
        odd = []
       # answer = []
        for i in range(len(A)):
            if(A[i]%2 == 0):
                even.append(A[i])
            else:
                odd.append(A[i])
       # answer = even + odd
        return even + odd
        