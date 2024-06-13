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
