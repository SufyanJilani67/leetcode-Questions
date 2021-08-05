class Solution(object):
    def makeGood(self, s):
        """
        :type s: str
        :rtype: str
        """
        stack = []
        for i in s:
            if len(stack)==0:
                stack.append(i)
            elif stack[-1]==i.swapcase():
                stack.pop()
            else:
                stack.append(i)
        return "".join(stack)
        