"""
Problem: Zigzag Conversion (LeetCode #6)

The string "PAYPALISHIRING" is written in a zigzag pattern on n rows as:
P   A   H   N
A P L S I I G
Y   I   R

Approach: Row-by-row construction
- Create arrays for each row
- Place characters in a zigzag pattern by calculating their row indices
- For each row, add the main character and diagonal character (if applicable)

Time Complexity: O(n) - Iterate through string once, O(n) to join result
Space Complexity: O(n) - Store entire string in rows

Key Points:
- Cycle length = 2 * (numRows - 1)
- Handle first, middle, and last rows differently (first/last have no diagonals)
- For middle rows, add both main and diagonal characters
"""

class Solution(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        # Base case: if only 1 row or string shorter than rows, no zigzag needed
        if numRows == 1 or numRows > len(s):
            return s
        
        # Initialize row arrays to store characters
        rows = [""] * numRows
        i = 0
        # Cycle length is the distance before a character repeats in the same row
        cycle = 2 * (numRows - 1)
        
        # Process each row
        while i < numRows:
            j = i  # Start position for this row
            # Add characters to current row
            while j < len(s):
                # Add the main character from the zigzag pattern
                rows[i] += s[j]
                # Calculate position of the diagonal character on the same row
                diag = j + cycle - 2 * i
                # Add diagonal character if it exists (not for first/last row)
                if i != 0 and i != numRows - 1 and diag < len(s):
                    rows[i] += s[diag]
                # Move to next position in the cycle for this row
                j += cycle
            i += 1
        
        # Concatenate all rows to get final result
        return "".join(rows)
