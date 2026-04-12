"""
Problem: Palindrome Number (LeetCode #9)

Given an integer x, return true if x is a palindrome, and false otherwise.

Approach: String conversion and comparison
- Convert integer to string
- Compare with its reverse
- Return true if they match

Time Complexity: O(log n) - Number of digits in integer
Space Complexity: O(log n) - String representation of integer

Key Points:
- Simple approach: convert to string and compare
- Note: Negative numbers are not palindromes (due to minus sign)
- Palindrome property is symmetric around center digit(s)
"""

class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        # Convert to string and compare with reverse
        # String reversal using slicing [::-1]
        return str(x) == str(x)[::-1]