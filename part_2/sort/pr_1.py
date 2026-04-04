"""
<< 위에서 아래로 (p.178) >>
    입력:
        첫째줄:
            N
        둘째줄:
            N개의 수 입력
"""
import sys
input=sys.stdin.readline

N=int(input().strip())
arr=[int(input().strip()) for _ in range(N)]

arr=sorted(arr,reverse=True) # 내림차순 정렬
print(arr)
