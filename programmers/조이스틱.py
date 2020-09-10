import string


def solution(name):
    answer = 0
    name = list(name)
    length = len(name)

    # first
    first_count = length - 1
    for i in range(length-1, 0, -1):
        if name[i] != 'A':
            break
        first_count -= 1

    # second
    second_count = length - 1
    for i in range(1, length):
        if name[i] != 'A':
            break
        second_count -= 1

    # third
    third_count = 0
    for i in range(1, length):
        pivot = i
        if name[i] == 'A':
            third_count *= 2
            break
        third_count += 1

    for i in range(length, pivot-1, -1):
        if ''.join(name[pivot:i]) == 'A' * (i-pivot):
            break
        third_count += 1

    answer += min(first_count, second_count, third_count)

    # counting alphabet
    for ch in name:
        answer += count_moving(ch)

    return answer


def count_moving(target):
    if target == 'A':
        return 0

    alpha_list = string.ascii_uppercase
    mid = len(alpha_list) // 2
    alpha_list = alpha_list[mid:] + alpha_list[:mid]

    count = 0
    for ch in alpha_list:
        if ch == target:
            break
        count += 1

    count = count - alpha_list.index('A')
    return abs(count)



"""
풀이요약

해당 문제는 두 가지 문제로 분리할 수 있다.
1. 조이스틱을 좌우로 움직일 때 어떻게하면 최단 거리로 움직일 수 있는지
2. A에서 지정하고자 하는 문자열까지의 거리

두 번째의 경우 간단하나 1번이 다시 세 가지 케이스로 나뉜다.
1. 우측으로 쭉 가는 경우
2. 역방향으로 쭉 가는 경우
3. 우측으로 가다가 방향 전환

첫 번째는 역방향에서 'A'가 아닌 문자열이 나올 때까지의 개수 빼줌
두 번째는 첫 번째의 경우와 반대
세 번째는 우측으로 가다가 A를 만나는 경우 현재 까지의 거리를 두배 곱해주고 역방향에서 시작한다.
    이때 인덱스 번호를 이용해서 남아 있는 원소들이 전부 A면 종료한다.
"""
