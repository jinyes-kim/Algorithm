def solution(N, M):
    answer = 0
    pivot = 0
    check_list = [False] * N

    while check_list[pivot] != True:
        check_list[pivot] = True
        pivot = (pivot + M) % N
        answer += 1

    return answer

"""
퍼포먼스에서 걸림
"""