def maxProfit(prices):
    min_price = float('inf')  # Set to positive infinity initially
    max_profit = 0

    for price in prices:
        if price < min_price:
            min_price = price  # Found a lower price to buy
        elif price - min_price > max_profit:
            max_profit = price - min_price  # Found a better profit

    return max_profit


# You can test the function here
if __name__ == "__main__":
    prices = [7, 1, 5, 3, 6, 4]
    print("Max Profit:", maxProfit(prices))

    prices2 = [7, 6, 4, 3, 1]
    print("Max Profit:", maxProfit(prices2))