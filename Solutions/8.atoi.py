"""
Problem: String to Integer (atoi) (LeetCode #8)

Implement the myAtoi(string s) function, which converts a string to a 32-bit signed integer.
Algorithm:
1. Skip leading whitespace
2. Check for +/- sign
3. Read digits until non-digit character
4. Clamp to 32-bit integer range

Approach: Character-by-character parsing with state machine concept
- Strip leading whitespace
- Handle optional sign character
- Parse digit characters one by one
- Stop at first non-digit
- Clamp result to 32-bit range

Time Complexity: O(n) - Scan through string once
Space Complexity: O(1) - Only store result integer

Key Points:
- Handle leading whitespace with lstrip()
- Check for sign before digits
- Stop parsing at non-digit characters
- Clamp result to [-2^31, 2^31 - 1]
"""

class Solution(object):
    def myAtoi(self, s):
        """
        :type s: str
        :rtype: int
        """
        # Flag to track if number is negative
        neg = False
        res = 0
        
        # Remove leading whitespace
        s = s.lstrip()
        
        # Empty string after stripping whitespace
        if len(s) == 0:
            return 0
        
        # Check for sign character
        if s[0] == '-':
            neg = True
            s = s[1:]
        elif s[0] == '+':
            s = s[1:]
        
        # Parse digit characters
        for c in s:
            try:
                # Check if character is a digit
                int(c)
            except ValueError:
                # Stop at first non-digit character
                break
            else:
                # Build number by shifting and adding new digit
                res = res * 10 + int(c)

        # Apply sign
        res = -res if neg else res
        
        # Clamp to 32-bit signed integer range [-2^31, 2^31 - 1]
        return min(2**31 - 1, max(-2**31, res))