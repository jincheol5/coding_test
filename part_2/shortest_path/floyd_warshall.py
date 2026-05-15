"""
<<플로이드 워셜 알고리즘>>
모든 지점에서 다른 모든 지점까지의 최단 경로를 모두 구해야 하는 경우.
다이나믹 프로그래밍으로 분류.

알고리즘 원리:


"""
import sys
input=sys.stdin.readline

INF=int(1e9)

N,M=map(int,input().split()) # N: node 수, M: edge 수


# 2차원 리스트를 만들고, 모든 값을 무한으로 초기화
distance=[[INF] * N for _ in range(N)]

# 자기 자신에서 자기 자신으로 가는 비용은 0으로 초기화
for i in range(N):
    distance[i][i]=0

# 각 간선에 대한 정보를 입력받아, 그 값으로 초기화
for _ in range(M):
    src,tar,weight=map(int,input().split())
    distance[src][tar]=weight

### 점화식에 따라 플로이드 워셜 알고리즘을 수행
# src->tar 경로를 k를 통해 갱신
# k=중간에 거치는 노드
# k 단계에서의 distance[src][tar]은 중간 노드로 1 ~ k 까지만 사용했을 때의 최단 거리
for k in range(N):
    for src in range(N):
        for tar in range(N):
            distance[src][tar]=min(
                distance[src][tar],
                distance[src][k]+distance[k][tar]
            )

# All pairs 결과 출력
for src in range(N):
    for tar in range(N):
        if distance[src][tar]==INF:
            print(f"INFINITY",end=" ")
        else:
            print(distance[src][tar],end=" ")
    print()