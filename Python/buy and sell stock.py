class Solution(object):
    def maxProfit(self, prices):
        left=0
        right=left+1
        profit=0
        while right<len(prices):
            if prices[left]<prices[right]:
                profit=max(profit,prices[right]-prices[left])
                right+=1
            else:
                left=right
                right=left+1
        return (profit)
