def solution(n):
    answer = 0
    tmp_sum = 0
    
    for x in range(1, n+1):
        for y in range(x, n+1):
            tmp_sum += y
            if tmp_sum > n:
                tmp_sum = 0
                break
            
            elif tmp_sum == n:
                answer += 1
                tmp_sum = 0
                break
    
    return answer