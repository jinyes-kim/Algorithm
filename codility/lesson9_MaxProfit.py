"""
주식 최대 수익 내기

1. 다음 인덱스 가격이 더 작으면 피벗을 이동
2. 다음 인덱스 가격이 더 크면 임시 값 생성하고 answer과 비교

"""
def solution(A):
    if len(A) <= 1:
        return 0

    answer = 0
    pivot = A[0]

    for day in range(1, len(A)):
        if A[day] < pivot:
            pivot = A[day]
            continue

        tmp = A[day] - pivot
        if tmp > answer:
            answer = tmp
    return answer

print(solution([23171, 21011, 21123, 21366, 21013, 21367]))
