"""
<< 미로 탈출 (p.152) >>
입력:
    첫째줄:
        N
        M
    둘째줄:
        미로 정보 N x M
"""
import sys
input=sys.stdin.readline

N,M=map(int,input().split())
adj=[list(map(int,input().strip())) for _ in range(N)]

from collections import deque

dx=[-1,1,0,0]
dy=[0,0,-1,1]

def bfs(x,y):
    Q=deque()
    Q.append((x,y))
    # 큐가 빌 때까지 반복
    while Q:
        x,y=Q.popleft()
        # 현재 위치에서 네 방향으로의 위치 확인
        for i in range(4):
            nx=x+dx[i]
            ny=y+dy[i]
            # 미로 공간 벗어난 경우 무시
            if nx<0 or ny<0 or nx>=N or ny>=M:
                continue
            # 벽인 경우 무시
            if adj[nx][ny]==0:
                continue
            # 해당 노드를 처음 방문하는 경우에만 최단 거리 기록
            if adj[nx][ny]==1:
                adj[nx][ny]=adj[x][y]+1 # 이전 최단 거리+1
                Q.append((nx,ny))
    # 가장 오른쪽 아래까지의 최단 거리 반환
    return adj[N-1][M-1]
print(bfs(0,0))