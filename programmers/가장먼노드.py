# 1. generate graph
# 2. find max depth
# 3. check depth & count


def solution(n, edge):
    answer = 0

    # step 1
    # initial graph
    weight = {str(edge): float("inf") for edge in range(1, n+1)}
    graph = {str(x): [] for x in range(1, n+1)}

    # add edge point
    for start, end in edge:
        graph[str(start)].append(end)
        graph[str(end)].append(start)

    # step 2
    # search graph depth from vertex '1'
    bfs_graph = bfs(graph, 1, weight)
    target = 0
    for count in bfs_graph.values():
        if count > target:
            target = count

    # step 3
    # count target
    for count in bfs_graph.values():
        if count == target:
            answer += 1

    return answer


def bfs(graph, start, weight):
    result, visit = [], []
    visit.append((start, 0))

    while visit:
        node = visit.pop(0)

        if weight[str(node[0])] > node[1]:
            weight[str(node[0])] = node[1]
            visit.extend([(x, node[1]+1) for x in graph[str(node[0])]])

    return weight


"""
노드 깊이 세는 알고리즘에서 머리 쥐나느라 미칠뻔했다..

요약
1. 그래프와 가중치 지표 생성
2. bfs 구조 - 큐에 노드와 가중치 인큐
3. 큐에 들어온 노드와 가중치가 현재 저장된 것 보다 작으면 교체


"""