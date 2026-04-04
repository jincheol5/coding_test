"""
벨만 포드 알고리즘
"""
import sys
input=sys.stdin.readline

INF=int(1e9)

N,M=map(int,input().split()) # N: node 수, M: edge 수
src_id=int(input().strip())

# 최단거리 정보 테이블
gamma_table={node:INF for node in range(N)}
gamma_table[src_id]=0

# 각 노드에 연결되어 있는 노드에 대한 정보를 담는 리스트 만들기
adj=[[] for _ in range(N)]

for _ in range(M):
    src,tar,weight=map(int,input().split())
    adj[src].append((tar,weight))

def bellman_ford_step(src_id:int,queue:set=None,init:bool=False):
    next_queue=set()
    if init:
        next_queue.add(src_id)
    else:
        for src in queue:
            for (tar,weight) in adj[src]:
                if gamma_table[src]+weight<gamma_table[tar]: 
                    # 새로운 최단 거리 발견하면 업데이트 후 다음 큐에 tar 삽입
                    gamma_table[tar]=gamma_table[src]+weight
                    next_queue.add(tar)
    return next_queue

def bellman_ford(src_id:int):
    queue=bellman_ford_step(src_id=src_id,init=True)
    while True:
        if not queue:
            break
        else:
            queue=bellman_ford_step(
                src_id=src_id,
                queue=queue,
                init=False
            )

bellman_ford(src_id=src_id)

for key,value in gamma_table.items():
    if value==INF:
        value=-1
    print(f"{src_id} to {key} shortest_path distance: {value}")

# 음의 싸이클 확인 필요 -> 특정 노드가 N번 이상 큐에 들어오는 경우 음의 싸이클 존재