"""
다익스트라 알고리즘
    음의 간선 없어야 함
"""
import sys
input=sys.stdin.readline

INF=int(1e9)

N,M=map(int,input().split()) # N: node 수, M: edge 수
src_id=int(input().strip())

# 최단거리 정보 테이블
distance=[INF for _ in range(N)]
distance[src_id]=0

# 방문 정보 
visited=[False for _ in range(N)]
visited[src_id]=True

# 각 노드에 연결되어 있는 노드에 대한 정보를 담는 리스트 만들기
adj=[[] for _ in range(N)]

for _ in range(M):
    src,tar,weight=map(int,input().split())
    adj[src].append((tar,weight))

def find_shortest_distance_node():
    # 방문하지 않은 노드 중에서, 가장 최단 거리가 짧은 노드 id 반환
    min_value=INF
    node_id=0
    for i in range(N):
        if distance[i]<min_value and not visited[i]:
            min_value=distance[i]
            node_id=i
    return node_id

def dijkstra(src_id:int):
    # 시작 노드에 대해서 초기화
    """
    """