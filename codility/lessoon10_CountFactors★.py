"""
약수의 개수를 구하는 문제

예를 들어서 25의 약수의 개수면 1,5,25 인데
이때 5 * 5가 25와 같아진다는 점과
전체 약수의 개수 반만 알아도 된다는 점을 알아야 한다.

num * num 이 N보다 작아지는 시점까지 약수인지 확인하고
맞다면 +2 , 아니면 숫자 + 1

25에서 5와 같은 경우는 5가 두 개인데, 1개로만 취급한다.
따라서 num * num == N이 되는 케이스만 마지막에 +1 로 처리한다.

"""


def solution(N):
    if N == 1:
        return 1

    answer = 0
    num = 1
    while num * num < N:
        if N % num == 0:
            answer += 2
            num += 1
        else:
            num += 1

    if num * num == N:
        answer += 1

    return answer
