
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices)==0:
            return 0
        
        buy = prices[0]
        mx_profit = 0

        for i in range(1,len(prices)):
            
            profit = prices[i]-buy
            
            if profit>mx_profit:
                mx_profit = profit

            if buy>prices[i]:
                buy = prices[i]
        
        return mx_profit
    
