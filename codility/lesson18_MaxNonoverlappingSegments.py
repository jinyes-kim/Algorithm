def solution(A, B):
    length = len(A)
    if length == 0:
        return 0

    count = 1
    end_point = B[0]
    for idx in range(1, length):
        if end_point < A[idx]:
            count += 1
            end_point = B[idx]

    return count