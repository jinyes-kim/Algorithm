"""
전체 어레이에서 중복 제거한, 고유 숫자의 개수를 리턴
ex) 1,1,1,2,2,3 이면 1, 2, 3이므로 3을 리턴
"""

def solution(A):
    dummy_set = set()

    for num in A:
        dummy_set.add(num)

    return len(dummy_set)
