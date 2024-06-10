def maxProfit(prices):
        maxProfit = 0
        val = prices[0]
        for i in range(1, len(prices)):
            val = min(val, prices[i])
            maxProfit = max(maxProfit, prices[i] - val )
        return maxProfit
