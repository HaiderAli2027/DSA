# class Solution(object):
#     def maxProfit(self, prices):
#         """
#         :type prices: List[int]
#         :rtype: int
#         """
#         if not prices:
#             return 0
            
#         min_price = float('inf')
#         max_pro = 0
        
#         for price in prices:
#             if price < min_price:
#                 min_price = price
#             elif price - min_price > max_pro:
#                 max_pro = price - min_price
                
#         return max_pro

class Solution(object):
    def maxProfit(self, prices):
        left, right = 0, 1
        maxProfit = 0
        
        while right < len(prices):
            if prices[left] < prices[right]:
                profit = prices[right] - prices[left]
                maxProfit = max(maxProfit, profit)
            else:
                left = right
            right += 1
        return maxProfit

print(Solution().maxProfit([7,1,5,3,6,4])) # Output: 5
print(Solution().maxProfit([7,6,4,3,1,0,1])) # Output: 1