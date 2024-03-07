class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        ans = 0
        tmp_list = [0]

        for i in range(len(prices)):
            cnt = i+1
            current = prices[i]
            for j in range(len(prices)-cnt):
                profit = prices[cnt] - current
                tmp_list.append(max(profit, 0))
                cnt += 1
            
        ans = max(tmp_list)
        return ans