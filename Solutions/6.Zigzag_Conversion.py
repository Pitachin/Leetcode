class Solution(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        if numRows == 1 or numRows > len(s): #Base case
            return s
        rows = [""] * numRows # save strs in each row
        i = 0
        cycle = 2*( numRows - 1 )
        while i < numRows:
            j = i
            while j < len(s):
                rows[i] += s[j]
                diag = j + cycle - 2 * i # the dist between j and next diag element on the same row...
                if i != 0 and i != numRows - 1 and diag < len(s):
                    rows[i] += s[diag]
                j += cycle
            i += 1
        return "".join(rows)
