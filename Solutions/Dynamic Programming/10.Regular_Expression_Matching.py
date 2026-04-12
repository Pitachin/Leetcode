"""
Problem: Regular Expression Matching (LeetCode #10)

Given an input string s and a pattern p, implement regular expression matching with support for
'.' (matches any single character) and '*' (matches zero or more of the preceding element).

Approach: Dynamic Programming (2D DP Table)
- dp[i][j] = whether first i characters of s match first j characters of p
- Rows: characters in s (index 0 to len(s))
- Cols: characters in p (index 0 to len(p))
- Base case: dp[0][0] = True (empty string matches empty pattern)

Transition:
- If p[j-1] == '*': Can match zero times (dp[i][j-2]) or match one/more times (dp[i-1][j])
- If p[j-1] == '.' or p[j-1] == s[i-1]: Characters match (dp[i-1][j-1])
- Otherwise: No match

Time Complexity: O(m*n) - m = len(s), n = len(p)
Space Complexity: O(m*n) - 2D DP table

Key Points:
- Handle '*' (zero or more matches) vs regular character
- Handle '.' (any single character) wildcard
- Careful with '*' handling: can match 0 or multiple preceding chars
"""

class Solution(object):
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        # dp[i][j] = whether s[0:i] matches p[0:j]
        # dp table has dimensions (len(s)+1) x (len(p)+1) to include empty string
        dp = [[False] * (len(p)+1) for _ in range(len(s)+1)]
        
        # Base case: empty string matches empty pattern
        dp[0][0] = True

        # Initialize first row: handle patterns like "a*b*c*" that can match empty string
        # Only '*' can match empty string if it follows a character
        for j in range(2, len(p) + 1):
            if p[j-1] == '*':
                # "x*" can match empty string, so check if pattern before "x*" matches empty
                dp[0][j] = dp[0][j-2]
        
        # Fill the DP table
        for i in range(1, len(s) + 1):
            for j in range(1, len(p) + 1):
                if p[j - 1] == '*':
                    # '*' case: matches zero or more of preceding character p[j-2]
                    # Option 1: Match zero occurrences of preceding character
                    dp[i][j] = dp[i][j-2]
                    # Option 2: Match one or more occurrences if preceding char matches
                    if p[j - 2] == s[i - 1] or p[j - 2] == '.':
                        dp[i][j] = dp[i][j-2] or dp[i - 1][j]
                elif p[j-1] == s[i-1] or p[j-1] == '.':
                    # Current characters match (or pattern has '.' wildcard)
                    dp[i][j] = dp[i-1][j-1]
                # else: characters don't match, dp[i][j] remains False
    
        # Return whether entire string s matches entire pattern p
        return dp[len(s)][len(p)]
