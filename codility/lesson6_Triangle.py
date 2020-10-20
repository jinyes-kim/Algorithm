"""
3개 골라서
A + B > C
B + C > A
C + A > B
만족하는 케이스가 있는지 검사

"""

def solution(A):
    A.sort()
    for idx in range(len(A)-2):
        if A[idx] + A[idx+1] > A[idx+2] and \
                A[idx+1] + A[idx+2] > A[idx] and \
                A[idx+2] + A[idx] > A[idx+1]:
            return 1

    return 0