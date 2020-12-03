# map 활용
def solution(n):
    answer = list(str(n))
    answer = list(map(int, answer))
    return sum(answer)

# hard coding
def solution(n):
    split_list = list(str(n))
    answer = [int(n) for n in split_list]
    return sum(answer)

