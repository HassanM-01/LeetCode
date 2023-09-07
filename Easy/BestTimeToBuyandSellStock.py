def maxProfit(prices):
    profit = 0  # initialize profit to zero
    buy = prices[0]  # initialize buy to first item in index

    for sell in prices[1:]:  # loop starting from 2nd item or index 1
        if sell > buy:  # check if sell is greater than buy
            profit = max(profit, sell - buy)  # calculate if profit is greater than current max profit
        else:
            buy = sell  # move buy pointer to current item

    return profit



