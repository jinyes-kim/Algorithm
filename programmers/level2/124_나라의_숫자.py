def solution(n):
    answer = ''
    numbers = ['4', '1', '2']

    while n:
        answer = numbers[n % 3] + answer
        n = n // 3 - (n % 3 == 0)

    return answer


참조 -

https://velog.io/@dramatic/Algorithm-124-%EB%82%98%EB%9D%BC%EC%9D%98-%EC%88%AB%EC%9E%90
