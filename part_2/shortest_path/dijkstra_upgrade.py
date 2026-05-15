"""
<<개선된 다익스트라>>
기존 알고리즘에서 현재 가장 가까운 노드를 저장하기 위한 목적으로만 우선순위 큐를 추가로 이용.
- Heap 자료구조 사용 for 우선순위 큐
- 최대 Heap: 우선순위 기준 값이 큰 데이터 먼저 삭제
- 최소 Heap: 우선순위 기준 값이 작은 데이터 먼저 삭제

다음 코드는 방향 그래프 전용
"""
import heapq
import sys
input=sys.stdin.readline

### 데이터셋 입력
N,M=map(int,input().split())
src_id=map(int,input().strip())
graph=[[] for _ in range(N+1)]
for i in range(M):
    src,tar,weight=map(int,input().split())
    graph[src].append((tar,weight))

### 초기 세팅
INF=int(1e9)
distance=[INF]*(N+1)

### 알고리즘
def upgrade_dijkstra(start,distance):
    # 시작 노드로 가기 위한 최단 경로는 0으로 설정하여 큐에 삽입
    q=[]
    heapq.heappush(q,(0,start))
    distance[start]=0
    while q:
        # 가장 최단 거리가 짧은 노드에 대한 정보 꺼내기
        dist,node=heapq.heappop(q)
        # 현재 노드가 이미 처리된 적이 있는 노드라면 무시
        if distance[node]<dist:
            continue
        # 현재 노드와 연결된 다른 인접한 노드들을 확인
        for neighbor,weight in graph[node]:
            cost=dist+weight
            # 현재 노드를 거쳐서 다른 노드로 이동하는 거리가 더 짧은 경우
            if cost<distance[neighbor]:
                distance[neighbor]=cost
                heapq.heappush(q,(cost,neighbor))

upgrade_dijkstra(start=src_id,distance=distance)