def solution(n):
    num_list = sorted(list(str(n)), reverse=True)
    answer = ''.join(num_list)
    return int(answer)