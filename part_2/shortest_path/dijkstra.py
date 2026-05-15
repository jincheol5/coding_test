"""
<<다익스트라 알고리즘>>
    - 특정한 노드에서 출발하여 다른 노드로 가는 각각의 최단 경로를 구해주는 알고리즘 
    - 음의 간선 없어야 함
    - 그리디 알고리즘으로 분류
    - 매번 가장 비용이 적은 노드를 선택해서 임의의 과정을 반복

<<알고리즘 원리>>
1. 출발 노드를 설정한다.
2. 최단 거리 테이블을 초기화한다.
    - 최단 거리 정보를 1차원 리스트에 저장하며 리스트를 계속 갱신
3. 방문하지 않은 노드 중에서 최단 거리가 가장 짧은 노드를 선택한다.
4. 해당 노드를 거쳐 다른 노드로 가는 비용을 계산하여 최단 거리 테이블을 갱신한다.
5. 위 과정에서 3과 4번을 반복한다.


<<입력 데이터>>

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

def dijkstra():
    # 최단 거리가 가장 짧은 노드
    for _ in range(N): # 최대 노드 수 만큼 반복
        node=find_shortest_distance_node()
        visited[node]=True # 방문 처리
        for (tar,weight) in adj[node]:
            if distance[node]+weight<distance[tar]:
                distance[tar]=distance[node]+weight

dijkstra(src_id=src_id)
for tar,dist in enumerate(distance):
    if dist==INF:
        dist=-1
    print(f"{src_id} to {tar} shortest_path distance: {dist}")


"""
개선된 다익스트라 알고리즘
    최단 거리 노드 탐색에 heap 자료구조 (완전 이진 트리) 적용 => 우선순위 큐
"""
