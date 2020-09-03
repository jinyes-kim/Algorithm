def solution(prices):
    length = len(prices)
    answer = []

    for a in range(length):
        tmp = 0
        for b in range(a+1, length):
            if prices[a] <= prices[b]:
                tmp += 1
            else:
                tmp += 1
                break
        answer.append(tmp)

    return answer