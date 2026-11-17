# Day 001 - Two Sum

**Topic:** Hashing

**Difficulty:** Easy

## Problem
Find two numbers whose sum equals the target
and return their indices.

## Approach
Use a dictionary to store previously
visited numbers and their indices.

For each number:
1. Calculate target - number.
2. Check whether the complement exists.
3. If found, return both indices.
4. Otherwise, store the current number.

## Complexity

Time: O(n)

Space: O(n)

## Key Learning
Hash maps can reduce the time complexity
of searching for complementary values.
