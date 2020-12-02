def solution(a, b):
    if a > b:
        tmp = b
        b = a
        a = tmp
        
    range_list = [x for x in range(a, b+1)]
    answer = sum(range_list)
    return answer
