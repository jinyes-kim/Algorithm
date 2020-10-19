
"""
last element move to first
right shift

1단계 - 이동방법
    마지막에서 처음으로 가는 방법?
    (현재 인덱스 + K) % 리스트 길이 = 새 인덱스


"""
def solution(A, K):
    # write your code in Python 3.6
    length = len(A)
    answer = [0 for _ in range(length)]
    
    for i, num in enumerate(A):
        answer[(i+K) % length] = num
    
    return answer


