from pprint import pprint
from collections import defaultdict
import heapq


def prim(start_node, edges):
    mst = []
    adjacent_edges = defaultdict(list)

    # 그래프 생성
    for weight, n1, n2 in edges:
        adjacent_edges[n1].append((weight, n1, n2))
        adjacent_edges[n2].append((weight, n2, n1))

    # 시작 노드, 완료 노드 초기화
    connected_nodes = set(start_node)
    candidate_edge_list = adjacent_edges[start_node]
    heapq.heapify(candidate_edge_list)

    # 후보 노드가 없을 때까지 루프
    while candidate_edge_list:
        weight, n1, n2 = heapq.heappop(candidate_edge_list)
        if n2 not in connected_nodes:
            connected_nodes.add(n2)
            mst.append((weight, n1, n2))
        
        # 방금 연결한 노드에서 갈 수 있는 노드들을 업데이이트
        for edge in adjacent_edges[n2]:
            if edge[2] not in connected_nodes:
                heapq.heappush(candidate_edge_list, edge)

    return mst


myedges = [
    [7, 'A', 'B'],
    [5, 'A', 'D'],
    [9, 'B', 'D'],
    [8, 'B', 'C'],
    [7, 'B', 'E'],
    [5, 'C', 'E'],
    [7, 'D', 'E'],
    [6, 'D', 'F'],
    [8, 'E', 'F'],
    [9, 'E', 'G'],
    [11, 'F', 'G'],
]

pprint(prim('A', myedges))

"""
시간 복잡도는 while 루프에서
간선의 개수 E 와 다시 노드에서 간선의 개수가 추가되는 log E개를 곱한 값

O(E log E)

"""