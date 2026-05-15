"""
<<서로소 집합을 활용한 undirected graph 내의 사이클 판별>>

알고리즘 원리:
    1. 각 간선을 확인하며 두 노드의 루트 노드를 확인한다.
    2. 루트 노드가 서로 다르다면 두 노드에 대하여 union 연산을 수행한다.
    3. 루트 노드가 서로 같다면 사이클이 발생한 것이다.
    4. 그래프에 포함되어 있는 모든 간선에 대하여 1,2,3번 과정을 반복한다.
"""
import sys
input=sys.stdin.readline

V,E=map(int,input().split())

parent_info=[v for v in range(V)]

def find(parent_info,v):
    if parent_info[v]!=v:
        return find(parent_info,parent_info[v])
    else:
        return v

def union(parent_info,a,b):
    a_p=find(parent_info,a)
    b_p=find(parent_info,b)
    if a_p==b_p:
        return False
    else:
        if a_p<b_p:
            parent_info[b_p]=a_p
        else:
            parent_info[a_p]=b_p
        return True

isCycle=False
for _ in range(E):
    src,tar=map(int,input().split())
    # 사이클이 발생한 경우 종료
    union_result=union(parent_info=parent_info,a=src,b=tar)
    if not union_result:
        isCycle=True
        break
print(isCycle)