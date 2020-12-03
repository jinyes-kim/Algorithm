def solution(n):
    divisor_list = isDivisor(n)
    return sum(divisor_list)


def isDivisor(number):
    divisor_list = []
    
    for n in range(1, number+1):
        if number % n == 0:
            divisor_list.append(n)
    
    return divisor_list