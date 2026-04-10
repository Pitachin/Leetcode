class Solution(object):
    def myAtoi(self, s):
        """
        :type s: str
        :rtype: int
        """
        neg = False # Assume it's positive
        res = 0
        s = s.lstrip() 
        if len(s) == 0:
            return 0
        if s[0] == '-':
            neg = True
            s = s[1:]
        elif s[0] == '+':
            s = s[1:]
        for c in s:
            try:
                int(c)
            except ValueError:
                break
            else:
                res = res * 10 + int(c)

        if res == "":
            return 0
        res = -res if neg else res
        return min(2**31 - 1, max(-2**31, res))