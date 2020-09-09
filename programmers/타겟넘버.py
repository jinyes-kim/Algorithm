

def solution(numbers, target):
    numbers.insert(0, 0)
    answer = dfs(numbers, [])
    return answer.count(target)


def dfs(numbers, stack, total=0, add=0):
    total += add
    numbers = numbers[1:]

    try:
        dfs(numbers, stack, total, numbers[0])
        dfs(numbers, stack, total, -numbers[0])
        
    except:
        stack.append(total)

    return stack




"""
풀이 요약

1. 각 원소마다 +, - 연산을 추가 해야함 -> dfs 연산
2. 트리 구조로 들어가다 더 이상 들어갈 곳이 없으면 stack 리스트에 추가
3. 최종적으로 stack 리스트 리턴

* 단 본 풀이방법에서는 시작할 때 루트 노드를 인위적으로 생성해줘야 함
"""
