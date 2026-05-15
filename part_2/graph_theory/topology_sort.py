"""
<<위상 정렬>>
방향 그래프의 모든 노드를 '방향성에 거스르지 않도록 순서대로 나열하는 것'.
진입차수: 특정한 노드로 들어오는 간선의 개수.

알고리즘 원리:
1. 진입차수가 0인 노드를 큐에 넣는다.
2. 큐가 빌 때까지 다음의 과정을 반복한다.
    - 큐에서 원소를 꺼내 해당 노드에서 출발하는 간선을 그래프에서 제거한다.
    - 새롭게 진입차수가 0이 된 노드를 큐에 넣는다.
    - 이 때 모든 원소를 방문하기 전에 큐가 빈다면 사이클이 존재한다고 판단할 수 있다.
        - 사이클에 포함되어 있는 원소들은 큐에 들어가지 못하기 때문. 
"""
import sys
input=sys.stdin.readline

V,E=map(int,input().split())
graph=[[] for i in range(V+1)]
indegree=[0 for _ in range(V+1)]
for _ in range(E):
    src,tar=map(int,input().split())
    indegree[tar]=indegree[tar]+1

from collections import deque

def topology_sort(graph,indegree):
    result=[]
    q=deque()

    # 처음 시작할 때는 진입차수가 0인 노드를 큐에 삽입
    for node in range(1,V+1):
        if indegree[node]==0:
            q.append(node)
    
    # 큐가 빌 때까지 반복
    while q:
        node=q.popleft()
        result.append(node)

        # 해당 원소와 연결된 노드들의 진압차수에서 1 빼기
        for neighbor in graph[node]:
            indegree[neighbor]-=1
            # 새롭게 진입차수가 0이 되는 노드를 큐에 삽입
            if indegree[neighbor]==0:
                q.append(neighbor)
    return result
result=topology_sort(graph,indegree)
print(result)