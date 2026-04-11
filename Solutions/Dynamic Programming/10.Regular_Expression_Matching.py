class Solution(object):
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """

        dp = [[False] * (len(p)+1) for _ in range(len(s)+1)] # 第一行表示了前j個 p中的字符， 第一列表示了前i個 s中的字符。
        dp[0][0] = True

        # 1. First row, i = 0
        for j in range(2, len(p) + 1): # 從第2個字符開始 有可能出現*
            if p[j-1] == '*':
                dp[0][j] = dp[0][j-2]
        # 2
        for i in range(1, len(s) + 1):
            for j in range(1, len(p) + 1):
                if p[j - 1] == '*':
                    dp[i][j] = dp[i][j-2] # 直接無視 x*
                    if p[j - 2] == s[i - 1] or p[j - 2] == '.': # p[j-2]: the preceding element
                        dp[i][j] = dp[i][j-2] or dp[i - 1][j]
                elif p[j-1] == s[i-1] or p[j-1] == ".":
                    dp[i][j] = dp[i-1][j-1]
    
        return dp[len(s)][len(p)]
