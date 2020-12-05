def solution(n, arr1, arr2):
    answer = []

    for idx in range(n):
        arr1_value = binary_func(arr1[idx], n)
        arr2_value = binary_func(arr2[idx], n)
        wall = match_number(n, arr1_value, arr2_value)
        answer.append(wall)

    return answer


def binary_func(number, n):
    answer = ''
    value = number

    while value > 1:
        mod = value % 2
        value = value // 2
        answer += str(mod)

    answer += str(value)

    if len(answer) < n:
        dummy = n - len(answer)
        answer += dummy * '0'

    return answer[::-1]


def match_number(n, arr1_num, arr2_num): 
    result = ''

    for idx in range(n):
        if arr1_num[idx] == '0' and arr2_num[idx] == '0':
            result += ' '
        else:
            result += '#'

    return result


#print(solution(6, [46, 33, 33 ,22, 31, 50], [27 ,56, 19, 14, 14, 10]))

"""
1 .두 배열의 숫자를 2진법으로 변환
    이때 자릿수를 n에 맞춰서 보정 (남는 칸은 모두 0으로 채워주어야 한다.)

2. 2진법으로 변환한 두 숫자를 비교해서 두 칸 모두 0이면 공백 나머지는 #으로 채운다.
"""
