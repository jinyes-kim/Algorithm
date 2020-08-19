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