"""
Problem: Climbing Stairs (LeetCode #70)

You are climbing a staircase. It takes n steps to reach the top.
Each time you can climb 1 or 2 steps. In how many distinct ways can you climb to the top?

Approach: Dynamic Programming (1D DP Array)
- dp[i] = number of ways to reach step i
- At each step i, you can either come from step i-1 (1 step up) or step i-2 (2 steps up)
- Base cases: dp[0] = 1 (one way to reach start), dp[1] = 1 (one way to reach step 1)
- Recurrence: dp[i] = dp[i-1] + dp[i-2]

This is essentially the Fibonacci sequence!

Time Complexity: O(n) - Fill dp array for n steps
Space Complexity: O(n) - 1D DP array of size n+1

Key Points:
- Classic DP problem
- At each step, sum ways to reach previous two steps
- Can be optimized to O(1) space with two variables
- Also solvable with Fibonacci closed-form or recursion with memoization
"""

class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        # dp[i] represents the number of distinct ways to climb to step i
        dp = [0] * (n + 1)
        
        # Base cases
        dp[0] = 1  # One way to stay at ground (start position)
        dp[1] = 1  # One way to reach step 1 (1 step up)
        
        # Fill DP array: at each step, add ways from previous two steps
        for i in range(2, n + 1):
            # Can reach step i from step (i-1) with 1 step or from step (i-2) with 2 steps
            dp[i] = dp[i - 1] + dp[i - 2]
        
        # Return number of ways to reach step n
        return dp[n]