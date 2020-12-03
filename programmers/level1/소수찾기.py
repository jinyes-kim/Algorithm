import math


def solution(n):
    answer = 0

    for n in range(2, n + 1):
        if prime(n):
            answer += 1

    return answer


def prime(number):
    for n in range(2, int(math.sqrt(number))+1):
        if number % n == 0:
            return False

    return True


"""
*알아야하는 점

소수는 해당 숫자의 제곱근까지만 체크 해보면 알 수 있다

"""