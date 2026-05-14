from collections import deque
"""
BFS
1. 탐색 시작 노드를 큐에 삽입하고 방문 처리를 한다.
2. 큐에서 노드를 꺼내 해당 노드의 인접 노드 중에서 방문하지 않은 노드를 모두 큐에 삽입하고 방문처리를 한다.
3. 2번의 과정을 더 이상 수행할 수 없을 때까지 반복한다. 
"""
def BFS(graph,src,visited):
    """
    """
    queue=deque()
    queue.append(src)
    visited[src]=True
    # 큐가 빌 때까지 반복
    while queue:
        v=queue.popleft()
        print(f"{v} ",end="")
        # 해당 원소와 연결된, 아직 방문하지 않은 원소들을 큐에 삽입
        for neighbor in graph[v]:
            if not visited[neighbor]:
                queue.append(neighbor)
                visited[neighbor]=True

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
BFS(graph=graph,src=1,visited=visited)