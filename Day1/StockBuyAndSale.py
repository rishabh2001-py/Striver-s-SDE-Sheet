# ProblemLink  :https://leetcode.com/problems/best-time-to-buy-and-sell-stock/
# You are given an array prices where prices[i] is the price of a given stock on the ith day.
# You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock.
# # Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.
# Input: prices = [7,1,5,3,6,4]
# Output: 5
# Explanation: Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6-1 = 5.
# Note that buying on day 2 and selling on day 1 is not allowed because you must buy before you sell


def main():
    def maxProfit(prices):

            n= len(prices)
            profit = 0
            curmax = prices[n-1]
            for i in range(n-2,-1,-1):

                if prices[i] < curmax:
                    profit = max(profit,curmax-prices[i])

                curmax = max(curmax,prices[i])

            return profit
    prices = [7,1,5,8,10,0]
    print(maxProfit(prices))

main()