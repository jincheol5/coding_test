"""
<< 음료수 얼려 먹기 (p.149) >>
입력:
    첫번째 줄
        N
        M
    두번째 줄
        N x M 얼음틀 형태 제시
        0: 구멍 뚫려 있음
        1: 구멍 없음

"""
import sys
input=sys.stdin.readline

N,M=map(int,input().split())
adj=[list(map(int,input().split())) for _ in range(N)]


def dfs(x,y):
    # 주어진 범위를 벗어나는 경우에는 즉시 종료
    if x<0 or x>=N or y<0 or y>=M:
        return False

    # 현재 노드를 아직 방문하지 않았다면
    if adj[x][y]==0:
        # 해당 노드 방문 처리
        adj[x][y]=1
        # 상,하,좌,우 위치도 모두 재귀적으로 호출
        dfs(x-1,y)
        dfs(x,y-1)
        dfs(x+1,y)
        dfs(x,y+1)
        return True
    else:
        return False

# 모든 노드에 대하여 음료수 채우기
result=0
for x in range(N):
    for y in range(M):
        # 현재 위치에서 DFS 수행
        if dfs(x,y)==True:
            result+=1
print(result)