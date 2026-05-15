"""
<<최소 신장 트리>>
신장 트리: 
    - 하나의 그래프가 있을 때 모든 노드를 포함하면서 사이클이 존재하지 않는 부분 그래프.
    - 모든 노드가 포함되어 서로 연결되면서 사이클이 존재하지 않는다는 조건은 트리의 성립 조긴이기도 함.

<<크루스칼 알고리즘>>
신장 트리 중에서 최소 비용으로 만들 수 있는 신장 트리를 찾는 알고리즘.
그리디 알고리즘으로 분류됨.
서로소 집합 연산 사용하기 때문에 무방향 그래프에 대해서만 유효.

알고리즘 원리:
    1. 간선 데이터를 비용에 따라 오름차순 정렬
    2. 간선을 하나씩 확인하며 현재의 간선이 사이클을 발생시키는지 확인.
        - 사이클이 발생하지 않는 경우 최소 신장 트리에 포함.
        - 사이클이 발생하는 경우 최소 신장 트리에 포함시키지 않음.
    3. 모든 간선에 대하여 2번 과정을 반복.
"""
import sys
input=sys.stdin.readline

V,E=map(int,input().split())

edges=[]
for _ in range(E):
    src,tar,weight=map(int,input().split())
    edges.append((src,tar,weight))
edges.sort(key=lambda x:x[2])

parent=[v for v in range(V)]

def find(parent,v):
    if parent[v]!=v:
        return find(parent,parent[v])
    else:
        return v

def union(parent,a,b):
    a_p=find(parent,a)
    b_p=find(parent,b)
    if a_p==b_p:
        return False
    else:
        if a_p<b_p:
            parent[b_p]=a_p
        else:
            parent[a_p]=b_p
        return True

tree_edges=[]
cost=0
for edge in edges:
    src,tar,weight=edge
    is_union=union(parent,src,tar)
    if is_union:
        tree_edges.append(edge)
        cost+=weight
print(tree_edges)
print(cost)

