"""
<< 숫자 카드 게임 >>
    N: 행의 개수
    M: 열의 개수
"""
import sys
input=sys.stdin.readline

N,M=map(int,input().split())
arr=[list(map(int,input().split())) for _ in range(N)]

max_value_cantidate=[]
for sub_arr in arr:
    max_value_cantidate.append(min(sub_arr))
print(max(max_value_cantidate))