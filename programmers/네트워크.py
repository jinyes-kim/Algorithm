def solution(n, computers):
    graph = {}

    # make graph
    for i, pc in enumerate(computers):
        node_list = []
        for j, edge in enumerate(pc):
            if edge != 0 and i != j:
                node_list.append(j + 1)

        graph[i+1] = node_list

    # dfs
    answer = []
    for i in range(1, n+1):
        network = set(dfs(graph, i))
        if network not in answer:
            answer.append(network)

    return len(answer)


def dfs(graph, start):
    result, visit = [], []
    visit.append(start)

    while visit:
        node = visit.pop()
        if node not in result:
            result.append(node)
            visit.extend(graph[node])

    return result


"""
풀이 요약

네트워크의 개수를 계산해야하는 문제이다.

포인트
1. 노드를 최대한 깊게 들어갈 수 있는 방법을 찾아야하므로 dfs를 활용한다. 
2. 입력 형태가 노드의 숫자가 아닌 인덱싱이므로 사전 전처리 작업이 필요하다.

3. 각 노드에서 dfs 를 수행하고 set함수를 이용해서 순서를 정리해준다. 
4. 순서를 정리한 network가 answer 리스트 안에 없는 경우 추가한다.(중복 제거)
5. answer 의 원소 개수가 네트워크의 개수이다.

"""