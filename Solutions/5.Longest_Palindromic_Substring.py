"""
Problem: Longest Palindromic Substring (LeetCode #5)

Given a string s, return the longest palindromic substring in s.

Approach: Center Expansion
- For each possible center (both single character and between two characters),
  expand left and right as long as characters match.
- Check both odd-length (single center) and even-length (center between chars) palindromes.

Time Complexity: O(n^2) - For each of n centers, we expand which takes O(n)
Space Complexity: O(1) - Only storing the longest palindrome found

Key Points:
- Handle both odd and even length palindromes
- Expand from center outward
- Track the longest palindrome found
"""

class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        longest = ''  # Store the longest palindrome found so far

        def center(left, right):
            # Expand around center while characters match
            while left >= 0 and right < len(s) and s[right] == s[left]:
                right += 1
                left -= 1
            # Return the palindromic substring
            return s[left + 1:right]

        # Try each position as a potential center
        for i in range(len(s)):
            # Check odd-length palindromes (single character as center)
            odd = center(i, i)
            if len(odd) > len(longest):
                longest = odd
            # Check even-length palindromes (between two characters as center)
            even = center(i, i+1)
            if len(even) > len(longest):
                longest = even

        return longest