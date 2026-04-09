class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        strx = str(abs(x))
        if x < 0:
            return 0 if -int(strx[::-1]) < -2**31 else -int(strx[::-1])
        else:
            return 0 if int(strx[::-1]) > 2**31 - 1 else int(strx[::-1])