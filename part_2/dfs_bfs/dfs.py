"""
DFS
1. 탐색 시작 노드를 스택에 삽입하고 방문 처리를 한다.
2-1. 스택의 최상단 노드에 방문하지 않은 인접 노드가 있으면 그 인접 노드를 스택에 넣고 방문 처리를 한다.
2-2. 방문하지 않은 인접 노드가 없으면 스택에서 최상단 노드를 꺼낸다.
3. 2번의 과정을 더 이상 수행할 수 없을 때까지 반복한다.

노드의 탐색 순서=스택에 들어간 순서 
"""

def DFS(graph,vertex,visited):
    """
    재귀함수로 DFS 간단하게 구현
    graph: 인접 리스트
    vertex: 현재 탐색 노드
    visited: 방문 정보
    """
    # 현재 노드 방문 처리
    visited[vertex]=True
    print(f"{vertex} vertex visited")
    for neighbor in graph[vertex]:
        if not visited[neighbor]:
            DFS(graph=graph,vertex=neighbor,visited=visited)

graph=[
    [],
    [2,3,8],
    [1,7],
    [1,4,5],
    [3,5],
    [3,4],
    [7],
    [2,6,8],
    [1,7]
]
visited=[False]*9
DFS(graph=graph,vertex=1,visited=visited)