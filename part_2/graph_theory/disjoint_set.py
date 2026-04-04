"""
서로소 집합 알고리즘
"""
import sys
input=sys.stdin.readline
N,M=map(int,input().split()) # N: node 수, M: edge 수

# 특정 원소가 속한 집합을 찾기
def find_parent(parent,node):
    # root node가 아니라면, root node 찾을 때까지 재귀적으로 호출
    if parent[node]!=node:
        return find_parent(parent,parent[node])
    return node

# 두 원소가 속한 집합을 합치기
def union_parent(parent,a,b):
    a_parent=find_parent(parent,a)
    b_parent=find_parent(parent,b)
    if a_parent<b_parent:
        parent[b_parent]=a_parent
    else:
        parent[a_parent]=b_parent

# 부모 테이블 초기화, 부모를 자기 자신으로 초기화
parent=[node for node in range(N)]

# union 연산을 각각 수행
for _ in range(M):
    a,b,=map(int,input().split())
    union_parent(parent,a,b)

# 각 원소가 속한 집합 출력
print(f"각 원소가 속한 집합: ",end="")
for node in range(N):
    print(f"{node} parent: {find_parent(parent,node)}",end=" ")

# 부모 테이블 내용 출력
print(f"부모 테이블: ")
for node,parent_id in enumerate(parent):
    print(f"{node}: {parent_id}",end=" ")