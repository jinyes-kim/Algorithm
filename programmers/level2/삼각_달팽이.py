def solution(n):
    answer = []
    dummy_list = [[] for _ in range(n)]
    last = sum([n for n in range(1, n+1)])
    number = 1
    idx = -1
    end_point = n-1
    pivot = 0
    reverse = False

    while number <= last:
        if reverse:
            idx = (idx-1) % n
        else:
            idx = (idx+1) % n

        if idx == end_point:
            length = (idx+1) - len(dummy_list[idx])
            dummy_list[idx] = dummy_list[idx][:pivot] \
                              + [n for n in range(number, number+length)] \
                              + dummy_list[idx][pivot:]
            number += length
            pivot += 1
            reverse = not reverse

        else:
            if len(dummy_list[idx]) <= idx:
                if reverse:
                    line_length = len(dummy_list[idx])
                    dummy_list[idx].insert(line_length-pivot+1, number)
                else:
                    dummy_list[idx].insert(pivot, number)
                number += 1

            if reverse == True and len(dummy_list[idx]) == idx + 1:
                reverse = False
                end_point -= 1

    for dummy in dummy_list:
        answer.extend(dummy)

    return answer

#solution(1000)

"""
숫자 채우는 건 까다롭지 않으나
정확한 위치로 이동시키는 게 까다로운 문제다.

3가지 패턴

1. 아래로
2. 엔드 포인트에서 전부 채우기(정방향에서 역방향으로의 조건)
3. 역방향 (2번 조건을 만족하면)
    - 삽입하다가 idx의 최대 길이만큼 전부 채워진 상태면 다시 리버스(역방향에서 정방향으로의 조건)
    - 이때 pivot += 1


*포인트는 정방향일 때랑 역방향일 때의 pivot이다.
엔드 포인트를 거치면 pivot은 1씩 커진다 

- 정방향이면 pivot 위치대로 적재한다.
- 역방향이면 현재 라인의 전체 길이에서 (pivot+1) 만큼 빼준 위치에 삽입한다.
- length - (pivot + 1)

* 역방향일 때는 뒤에서부터 앞으로 채운다.

"""