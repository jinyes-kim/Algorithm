"""
전형적인 스택 문제

브라켓 받아서 다 소진되면 1반환
아니면 0 반환
"""
def solution(S):
    stack = []
    for ch in S:
        if ch == '[' or ch == '{' or ch == '(':
            stack.append(ch)
        elif ch == ']' or ch == '}' or ch == ')':
            try:
                open_ch = stack.pop()
            except:
                return 0

            if open_ch == '[' and ch != ']':
                return 0
            elif open_ch == '{' and ch != '}':
                return 0
            elif open_ch == '(' and ch != ')':
                return 0

    if len(stack) != 0:
        return 0
    return 1