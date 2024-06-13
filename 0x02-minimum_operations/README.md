## Problem Description

In a text file, there is a single character 'H'. Your text editor can execute only two operations in this file:

Copy All: Copies all characters currently in the file.
Paste: Pastes the copied characters at the end of the current sequence.
Given a number n, write a method minOperations(n) that calculates the fewest number of operations needed to result in exactly n 'H' characters in the file.

## Solution Explanation

To determine the fewest number of operations needed, we use the concept of prime factorization:

# Operations:

Copy All: This copies all the characters currently in the file.
Paste: This pastes the copied characters at the end of the current sequence.

# Prime Factorization:

- By breaking down n into its prime factors, we can determine the sequence of multiplications that lead to n.
- Each prime factor represents a multiplication step that can be achieved through a Copy All followed by multiple Paste operations.

# Steps to Solve the Problem

1. Factorize n:

Decompose n into its prime factors. Each prime factor represents a multiplication step that can be achieved through a Copy All followed by multiple Paste operations.

2. Calculate Minimum Operations:

The sum of the prime factors of n will give the minimum number of operations required. This is because each prime factor corresponds to a series of Paste operations after a Copy All.

# Example Walkthrough

For n = 9:

Prime factorization of 9 is 3×3

This means we can reach 9 'H's by:
Starting with 1 'H'.

- Copy All (1 operation), Paste twice (2 operations) to get 3 'H's.
- Copy All (1 operation), Paste twice (2 operations) to get 9 'H's.
- Total operations: 1 (initial) + 2 + 1 + 2 = 6 operations.

# Code Explanation

- Initial Check:
  Checks if n is less than or equal to 1. If so, returns 0 because it's impossible to achieve the target with the given operations.
- Initialization:
  - Initializes operations to count the number of operations performed.
  - Initializes factor to 2, the smallest prime factor.
- Prime Factorization
  - A while loop runs as long as factor \* factor is less than or equal to n, ensuring only factors up to the square root of n are checked.
  - For each factor, a nested while loop divides n by the factor as long as n is divisible by that factor.
  - For each division, the factor is added to the operations count, representing a series of Copy All followed by Paste operations.
  - Updates n by dividing it by the current factor.
  - Increments the factor to check the next potential divisor.
- Handle Remaining Factor:
  - If after exiting the loop n is still greater than 1, it means n itself is a prime number greater than its square root. In this case, n is added to the operations count.
- Return the Result:
  - Returns the total number of operations accumulated in operations.
