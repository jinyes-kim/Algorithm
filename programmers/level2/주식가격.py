def solution(prices):
    answer = []
    length = len(prices)

    for stock in range(length):
        count = 0
        for next_stock in range(stock+1, length):
            if prices[stock] <= prices[next_stock]:
                count += 1
            else:
                count += 1
                break
        answer.append(count)
        
    return answer
