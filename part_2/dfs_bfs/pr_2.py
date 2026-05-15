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

mv_x=[-1,1,0,0]
mv_y=[0,0,-1,1]

def bfs(adj,x,y):
    q=deque()
    q.append((x,y))
    # 큐가 빌 때까지 반복
    while q:
        x,y=q.popleft()
        for i in range(4):
            next_x=x+mv_x[i]
            next_y=y+mv_y[i]
            # 현재 위치에서 네 방향으로의 위치 확인
            if next_x<0 or next_x>=N or next_y<0 or next_y>=M:
                continue
            # 벽인 경우 무시
            if adj[next_x][next_y]==0:
                continue
            # 해당 노드를 처음 방문하는 경우에만 최단 거리 기록
            if adj[next_x][next_y]==1: 
                adj[next_x][next_y]=adj[x][y]+1
                q.append((next_x,next_y))
    return adj[N-1][M-1]
print(bfs(adj,0,0))