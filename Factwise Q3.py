#Stock Prices
def max_profit(prices):
    if not prices or len(prices)==1:
        return 0
    
    max_profit=0
    min_price = prices[0]

    for price in prices:
        min_price=min(min_price,price)
        max_profit=max(max_profit,price-min_price)

    return max_profit
