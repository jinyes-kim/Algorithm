def solution(n):
    answer = 0
    pivot = binary(n)
    pivot_count = pivot.count('1')
    
    while True:
        n += 1
        pivot = binary(n)
        count = pivot.count('1')
        
        if count == pivot_count:
            return n
    

def binary(n):
    value = n
    result = ''

    while value > 1:
        mod = value % 2
        value //= 2
        result += str(mod)

    result += str(value)
    return result[::-1]