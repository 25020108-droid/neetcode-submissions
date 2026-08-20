class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_buy_price = float('inf') 
        max_profit = 0
        for current_price in prices:
            current_profit = current_price - min_buy_price
            if current_profit > max_profit:
                max_profit = current_profit
            if current_price < min_buy_price:
                min_buy_price = current_price
        return max_profit

