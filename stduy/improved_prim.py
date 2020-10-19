from pprint import pprint
from heapdict import heapdict
from collections import defaultdict


def prim(start, graph):
    # 그래프 생성
    my_graph = defaultdict(dict)
    
    for weight, n1, n2 in graph:
        my_graph[n1][n2] = weight
        my_graph[n2][n1] = weight

    # 자료구조 초기화 
    # key는 가중치를 저장할 heapdict(), 해당 자료구조는 힙이 적용된 사전이다.
    # pi는 추가될 간선이 어디에서 출발한 것인지에 관한 사전
    mst, key, pi, total_weight = list(), heapdict(), dict(), 0

    # 모든 간선에 대한 가중치를 초기화하고, 연결 노드를 초기화한다.
    # key는 heapdict() 타입이므로 요소가 추가될때마다 자동으로 정렬된다.
    for node in my_graph.keys():
        key[node] = float('inf')
        pi[node] = None

    # 시작 노드의 가중치와 연결노드를 0, 자기자신으로 초기화
    key[start], pi[start] = 0, start

    # 모든 간선이 mst에 추가될 때까지 루프
    while key:
        # 따라서 후보 간선을 key에 추가하면 가중치가 작은 요소부터 pop된다.
        current_node, current_keys = key.popitem()
        mst.append([pi[current_node], current_node, current_keys])
        total_weight += current_keys

        # 생성한 그래프에서 현재 노드에서 갈 수 있는 노드와 가중치 정보를 루프
        # 노드의 가중치를 업데이트 하는 key의 최신 값보다 가중치가 적다면 업데이트
        for adjacent, weight in my_graph[current_node].items():
            if adjacent in key and weight < key[adjacent]:
                key[adjacent] = weight
                pi[adjacent] = current_node
                # 여기서 업데이트한 가장 작은 가중치 노드가 위에서 다시 pop으로 연결

    return mst, total_weight


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
기본적인 프림의 시간 복잡도 O(E log E)

개선된 프림 알고리즘의 시간 복잡도 O(E log V)

E = edge
V = vertices
"""
