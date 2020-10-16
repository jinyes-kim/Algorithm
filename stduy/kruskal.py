from pprint import pprint

test_graph = {
    'vertices': ['A', 'B', 'C', 'D', 'E', 'F', 'G'],
    'edges': [
        (7, 'A', 'B'),
        (5, 'A', 'D'),
        (7, 'B', 'A'),
        (8, 'B', 'C'),
        (9, 'B', 'D'),
        (7, 'B', 'E'),
        (8, 'C', 'B'),
        (5, 'C', 'E'),
        (5, 'D', 'A'),
        (9, 'D', 'B'),
        (7, 'D', 'E'),
        (6, 'D', 'F'),
        (7, 'E', 'B'),
        (5, 'E', 'C'),
        (7, 'E', 'D'),
        (8, 'E', 'F'),
        (9, 'E', 'G'),
        (6, 'F', 'D'),
        (8, 'F', 'E'),
        (11, 'F', 'G'),
        (9, 'G', 'E'),
        (11, 'G', 'F')
    ]
}


parent = dict()
rank = dict()


def find(node):
    # path compression
    # 파라미터 노드의 부모 노드를 리턴
    if parent[node] != node:
        parent[node] = find(parent[node])
    return parent[node]


def union(node_v, node_u):
    root1 = find(node_v)
    root2 = find(node_u)

    # union by rank
    if rank[root1] > rank[root2]:
        parent[root2] = root1  # root2 의 랭크가 더 작으므로 root2의 부모 노드는 root2 본인에서 root1이 된다.
    else:
        parent[root1] = root2  # 위와 반대의 경우

        # 두 노드의 랭크가 같은 경우 root2의 랭크를 하나 더 올려준다.
        if rank[root1] == rank[root2]:
            rank[root2] += 1


def make_set(node):
    parent[node] = node
    rank[node] = 0

    """
    parent = {'A': 'A', 'B': 'B', ... } 노드의 부모를 자기자신으로 초기화
    rank = {'A': 0, 'B': 0, ...} 노드의 랭크(높이)를 0으로 초기화
    """


def kruskal(graph):
    mst = list()

    # 1. 초기화
    for node in graph['vertices']:
        make_set(node)

    """
    각 노드의 루트 노드를 저장할 딕셔너리와,
    각 노드의 랭크를 저장할 딕셔너리를 초기화
    """

    # 2. 간선 weight 기반 sorting
    edges = graph['edges']
    edges.sort()    # 정렬 방법을 커스텀할 수도 있다.
    """
    edges = (7, 'A', 'B'), (5, 'A', 'D'), (7, 'B', 'A'), (8, 'B', 'C') ...
    edges.sort() => (5, 'A', 'D'), (5, 'C', 'E'), (5, 'D', 'A'), (5, 'E', 'C')
    """

    # 3. 싸이클 검사 & 간선 연결
    for edge in edges:
        weight, node_v, node_u = edge

        # find 검사
        if find(node_v) != find(node_u):
            union(node_v, node_u)
            mst.append(edge)

    """
    과정 - edges 주석 기준
    
    1단계 
        1) A와 D의 루트가 다르다. 
        2) A와 D의 랭크 모두 0
        3) D가 A의 루트 노드가 되고 D의 랭크 ++
    
    2단계
        1) C의 루트 노드(C)와 E의 루트 노드(E)가 다르다.
        2) C와 E의 랭크 모두 0
        3) E가 C의 루트 노드가 되고 E의 랭크 ++
    
    3단계 
        1) D의 루트 노드(D) A의 루트 노드 (D) 가 같으므로 PASS
    .
    .
    .
    9단계 
        1) B의 루트 노드(D) 와 E의 루트 노드(E)가 다르다.
        2) D와 E의 랭크가 1로 같다.
        3) 따라서 E의 랭크를 ++ 하고 D의 루트 노드는 E가 된다.
    """

    return mst


pprint(kruskal(test_graph))


"""
시간복잡도 O(E log E)

O(V) - make-set
O(E log E) - sort the edge
O(E) - for each node 

"""