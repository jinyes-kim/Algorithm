def solution(priorities: list, location):
    answer = 1
    queue = [(b, a) for a, b in enumerate(priorities)]
    target = queue[location]

    while True:
        max_value = max(queue, key=lambda x: x[0])
        idx = queue.index(max_value)
        queue = queue[idx:] + queue[:idx]
        value = queue.pop(0)

        if value == target:
            return answer
        answer += 1

    return answer


#print(solution([1, 1, 9, 1, 1, 1], 0))

"""
우선순위 큐를 구현하는 것
단 문제에서 제시하는 방법을 살펴보면,

1. 제일 우선순위가 높은 요소 바로 직전까지의 요소는 잘라내서 다시 뒤로 붙여야 한다.
2. 배열에는 우선순위만 있고 문서를 구분할 수 있는 고유한 ID값은 없다 -> 문서 ID생성 
    - 따라서 문서의 ID값은 초기 인덱스 값으로 지정한다.

"""