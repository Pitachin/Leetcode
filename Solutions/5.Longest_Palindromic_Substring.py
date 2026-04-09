class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        longest = ''

        def center(left, right):
            while left >= 0 and right < len(s) and s[right] == s[left]:
                right += 1
                left -= 1
            return s[left + 1:right]

        for i in range(len(s)):
            odd = center(i, i)
            if len(odd) > len(longest):
                longest = odd
            even = center(i, i+1)
            if len(even) > len(longest):
                longest = even

        return longest