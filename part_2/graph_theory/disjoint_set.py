"""
<<서로소 집합 알고리즘>>
서로소 집합: 공통 원소가 없는 두 집합.
서로소 집합 자료구조: 
    - 서로소 부분 집합들로 나누어진 원소들의 데이터를 처리하기 위한 자료구조.
    - 연산:
        - union: 2개의 원소가 포함된 집합을 하나의 집합으로 합치는 연산
        - find: 특정한 원소가 속한 집합이 어떤 집합인지 알려주는 연산
    - 서로소 집합 자료구조를 구현할 때는 트리 자료구조를 이용하여 집합을 표현.
        
트리 자료구조를 이용하는 서로소 집합 계산 알고리즘:
    - union(A,B): 
        1. A집합과 B집합의 루트 노드 A'와 B'를 각각 찾는다.
        2. A'를 B'의 부모 노드로 설정한다(B'가 A'를 가리키도록 한다).
        3. 모든 union 연산을 처리할 때까지 1-2번 과정을 반복한다. 
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