def solution(N, stages):
    prob_list = []
    sorted_list = sorted(stages)
    length = len(stages)

    for n in range(1, N+1):
        if n == N+1:
            continue

        try:
            idx = sorted_list.index(n)
            fail = sorted_list.count(n)
            total = length - idx
            prob = fail / total
            prob_list.append([n, prob])

        except:
            prob_list.append([n, 0])

    prob_list.sort(key=lambda x: x[1], reverse=True)
    answer = [x[0] for x in prob_list]
    return answer

print(solution(5, [2, 1, 2, 6, 2, 4, 3, 3]))

"""
문제의 핵심은 루프를 돌면서 현재 숫자보다 크거나 같은 수가 몇개나 있는가이다.
가령 위 샘플 케이스를 정렬해보면 [1, 2, 2, 2, 3, 3, 4, 6]이다.

2랑 같거나 큰 수는 7개가 있으므로 스테이지 2에 도전한
유저는 7명이다. 그리고 실패한 인원은 2가 3개 있으므로 3명이다. 
따라서 실패 확률은 3/7이 된다.


1. 스테이지스 리스트를 정렬한다.
2. 숫자의 인덱스 넘버를 찾고 스테이지스 인풋값의 길이에서 뺀다 == 스테이지에 도전한 유저
3. 현재 숫자가 스테이지 리스트에 몇개 있는지 카운팅한다. == 스테이지에 도전했지만 실패한 유저
4. 확률은 3번의 경우 / 2번의 경우 다.
5. 예외처리 
    - 1~N+1까지 루프를 돌리므로 실패한 유저가 한 명도 없는 스테이지는 밸류 에러가 난다.
      따라서 예외처리를 해야하는 스테이지의 실패 확률은 0 이다.1

* 시작시 인풋값인 스테이지스를 정렬하고 시작하므로 동률인 경우 별도로 정렬해줄 필요가 없다.
"""
