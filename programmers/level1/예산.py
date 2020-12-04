def solution(d, budget):
    answer = 0
    d.sort()
    
    for team in d:
        if budget - team >= 0:
            answer += 1
            budget -= team
        else:
            break
        
    return answer
