def maxProfit(prices):
    min_price = float('inf')
    max_profit = 0

    for price in prices:
        min_price = min(min_price, price)
        profit = price - min_price
        max_profit = max(max_profit, profit)

    return max_profit


# Test cases
if __name__ == "__main__":
    test_cases = [
        ([7, 1, 5, 3, 6, 4], 5),
        ([7, 6, 4, 3, 1], 0),
        ([1, 2], 1),
        ([2, 4, 1], 2),
        ([3, 3, 3, 3], 0),
        ([8, 3, 10, 2, 12], 10)
    ]

    for prices, expected in test_cases:
        result = maxProfit(prices)
        print(f"Prices: {prices}")
        print(f"Maximum Profit: {result}")
        print(f"Expected: {expected}")
        print("Status:", "PASS" if result == expected else "FAIL")
        print("-" * 40)
