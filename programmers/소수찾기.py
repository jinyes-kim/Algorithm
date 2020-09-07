# permutaions / 순열
# combinations / 조합
from itertools import permutations


def solution(numbers):
    answer = 0
    number_bag = []
    total_list = []

    for num in numbers:
        number_bag.append(str(num))

    for n in range(len(numbers)):
        tmp = list(map(''.join, permutations(number_bag, n+1)))
        for unique in tmp:
            unique = int(unique)
            if unique not in total_list:
                total_list.append(unique)

    for num in total_list:
        if is_prime(int(num)):
            answer += 1

    return answer


def is_prime(number):
    length = number

    if number == 0 or number == 1:
        return False

    for a in range(2, length):
        if number % a == 0:
            return False
    return True
