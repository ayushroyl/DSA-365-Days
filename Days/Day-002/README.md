# Day 002 - Best Time to Buy and Sell Stock

## Problem
Given an array of stock prices, find the maximum profit
that can be achieved by buying once and selling once.

You must buy before you sell.

## Example

Input:
[7, 1, 5, 3, 6, 4]

Output:
5

Explanation:
Buy at price 1 and sell at price 6.

Maximum profit = 6 - 1 = 5.

## Approach: Greedy Algorithm

1. Initialize min_price with infinity.
2. Initialize max_profit with 0.
3. Traverse the prices array.
4. Update the minimum buying price.
5. Calculate today's possible profit.
6. Update maximum profit if today's profit is higher.
7. Return maximum profit.

## Complexity

- Time Complexity: O(n)
- Space Complexity: O(1)

## Concepts Learned

- Arrays
- Greedy Algorithm
- Minimum and Maximum
- Single-pass traversal
