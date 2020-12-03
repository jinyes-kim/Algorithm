def solution(n, m):
    answer = [gcd(n, m), lcm(n, m)]
    return answer


# Euclidean algorithm
def gcd(x, y):
    while x:
        x, y = y % x, x

    return y


def lcm(x, y):
    return x * y // gcd(x, y)
