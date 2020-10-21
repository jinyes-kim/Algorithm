"""
정렬했을 때 최댓값의 두 가지 케이스가 생긴다.

맨 뒤의 3개
앞의 음수 두개와 제일 끝의 양수 하나

전부 다 음수여도 제일 뒤의 값이 가장 크므로 상관없다.
"""
def solution(A):
    A.sort()
    return max(A[0]*A[1]*A[-1], A[-1]*A[-2]*A[-3])