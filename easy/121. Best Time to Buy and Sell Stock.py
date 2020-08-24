class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if not prices:
            return 0
        
        pivot = prices[0]
        answer = 0
        for n in range(1, len(prices)):
            if pivot > prices[n]:
                pivot = prices[n]
                continue

            tmp = prices[n] - pivot
            if tmp > answer:
                answer = tmp
        return answer