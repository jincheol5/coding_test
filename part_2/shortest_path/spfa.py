"""
Shortest Path Faster Algorithm (SPFA)
- 거리 갱신이 일어난 노드만 다시 검사

데이터셋:
6 11
1
1 2 2
1 3 5
1 4 1
2 3 3
2 4 2
3 2 3
3 6 5
4 3 3
4 5 1
5 3 1
5 6 2
"""
from collections import deque 
import sys
input=sys.stdin.readline

INF=int(1e9)

N,M=map(int,input().split()) # N: node 수, M: edge 수
src_id=int(input().strip())
graph=[[] for _ in range(N+1)]
for _ in range(M):
    src,tar,weight=map(int,input().split())
    graph[src].append((tar,weight))
distance=[INF]*(N+1) # 해당 노드까지의 최단 거리 기록

def SPFA(src,graph,distance):
    Q=deque()
    Q.append(src)
    distance[src]=0
    while Q:
        node=Q.popleft()
        for neighbor,weight in graph[node]:
            if distance[node]!=INF and distance[node]+weight<distance[neighbor]:
                distance[neighbor]=distance[node]+weight
                if neighbor not in Q:
                    Q.append(neighbor)

SPFA(src=src_id,graph=graph,distance=distance)
print(distance[1:])


# 음의 싸이클 확인 필요 -> 특정 노드가 N번 이상 큐에 들어오는 경우 음의 싸이클 존재