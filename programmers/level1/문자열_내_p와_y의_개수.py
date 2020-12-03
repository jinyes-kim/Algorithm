def solution(s: str):
    s = s.lower()
    p_count = s.count('p')
    y_count = s.count('y')

    return p_count == y_count
