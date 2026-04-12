"""
Problem: Reverse Integer (LeetCode #7)

Given a signed 32-bit integer x, return x with its digits reversed.
If reversing x causes the value to go outside the signed 32-bit integer range [-2^31, 2^31 - 1],
then return 0.

Approach: String conversion and validation
- Convert number to string and reverse it
- Handle negative sign separately
- Check bounds before returning (32-bit signed integer limits)

Time Complexity: O(log n) - Number of digits in integer
Space Complexity: O(log n) - String representation of integer

Key Points:
- Handle negative numbers carefully
- Check 32-bit overflow: [-2^31, 2^31 - 1]
- Return 0 if result is out of range
"""

class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        # Work with absolute value to simplify reversal
        strx = str(abs(x))
        
        # Handle negative numbers
        if x < 0:
            # Reverse and negate, check if within 32-bit range
            reversed_val = -int(strx[::-1])
            return 0 if reversed_val < -2**31 else reversed_val
        else:
            # Reverse positive number, check if within 32-bit range
            reversed_val = int(strx[::-1])
            return 0 if reversed_val > 2**31 - 1 else reversed_val