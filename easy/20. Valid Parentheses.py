class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) % 2 == 1:
            return False
        else:
            stack = []
            for ch in s:
                if ch == '[' or ch == '{' or ch == '(':
                    stack.append(ch)
                elif ch == ']' or ch == '}' or ch == ')':
                    try:
                        left = stack.pop()
                        right = ch
                    except:
                        return False

                    if left == '[' and right == ']':
                        continue
                    elif left == '{' and right == '}':
                        continue
                    elif left == '(' and right == ')':
                        continue
                    else:
                        return False

            if len(stack) != 0:
                return False
            return True
        
        
"""
자료구조 책에 나올 법한 풀이인데 속도, 메모리 사용량에서 비효율적이라는 결과가 나왔다.
인풋 문자열이 짝수가 아닌 경우 바로 false를 리턴하도록 바꿨다.

풀이 방법은 스택을 이용한 단순한 풀이 방법을 사용했다.

"""
