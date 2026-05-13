class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # lets say that we always buy first then sell 
        # it means left = buy, right = sell
        # where prices[i] is the price of NeetCoin on the ith day.
        # we can implement sliding window that left is buy right is sell
        # we only buy and sell (profit = sell - buy) when
        # sell > buy or no buy

        # Input: prices = [10,1,5,6,7,1]
        #                  b                             
        #                     s     
        # Output: 6

        buy, sell = 0, 0
        max_profit = 0

        for sell in range(1, len(prices)):
            if prices[sell] < prices[buy]:
                buy = sell
            else:
                profit = prices[sell] - prices[buy]
                max_profit = max(max_profit, profit)

        return max_profit
                
