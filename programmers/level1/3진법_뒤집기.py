def solution(n):
    third = func(n, 3)
    print(third)
    reverse_third = third[::-1]
    print(reverse_third)
    answer = cnuf(reverse_third)
    return answer


def func(number, N): # N 진수로 변환하는 함수
    answer = ''
    value = int(number)

    while value >= N:
        mod = value % N
        new_value = value // N
        answer += str(mod)
        value = new_value

    answer += str(value)
    return answer[::-1]


def cnuf(number):
    answer = 0
    value = str(number[::-1])
    pivot = 0

    for n in value:
        n = int(n)
        if n == 0:
            pivot += 1
            continue
        elif n == 1:
            answer += (3 ** pivot)
        elif n == 2:
            answer += (3 ** pivot) * 2
        else:
            raise Exception("3진수가 아님")
        pivot += 1

    return answer




"""
func 함수는 진수변환할 때 가져다가 쓸 수 있을 듯


1. 3진법 변환 후 뒤집기
2. 10진법으로 다시 만드는 방법
    2진법과 비슷하지만 3진법은 0, 1에 추가로 2가 있다. 
    
    pivot은 자릿수 (0부터 시작)
    
    0 = 0
    1 = 3
    2 = 3^pivot * 2
    
"""



