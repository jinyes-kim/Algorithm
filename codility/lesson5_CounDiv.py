"""
A~B 사이의 숫자에서 K로 나눠지는 수의 개수를 구한다.

1단계 - B에서 K로 나눠지는 수 개수 - A에서 K로 나눠지는 수 개수
2단계 - 그런데 B에는 A에도 포함이 된다. 따라서 만약 숫자 A가 K로 딱 떨어지는 경우 + 1 

"""

def solution(A, B, K):
    answer = B // K - A // K
    if A % K == 0:
        return answer + 1

    return answer