def solution(x, n):
    if x == 0:
        return [0] * n
    
    answer = []
    weight = 1
    
    if x < 0:
        weight = -1
        
    for n in range(x, x*n+weight, x):
        answer.append(n)
    return answer
