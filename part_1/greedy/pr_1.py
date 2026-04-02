"""
<< 큰 수의 법칙 >>
    N=입력 정수 수
    M=총 더하는 개수
    K=가능한 최대 반복 덧셈 수
"""
import sys
input=sys.stdin.readline

N,M,K=map(int,input().split())
arr=list(map(int,input().split()))

max_value=max(arr)
arr.remove(max_value)
sub_value=max(arr)

k=0
ans=0
for idx in range(M):
    if k<3:
        ans+=max_value
    else:
        ans+=sub_value
        k=0
    k+=1
print(ans)