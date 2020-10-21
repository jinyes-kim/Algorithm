def solution(K, A):
    total = 0
    answer = 0
    
    for num in A:
        total += num
        if total >= K:
            answer += 1
            total = 0

    return answer