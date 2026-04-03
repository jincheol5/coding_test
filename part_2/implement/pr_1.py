"""
<< 상하좌우 (p.110) >>
    N
    L: 왼쪽으로 한칸 
    R: 오른쪽으로 한칸
    U: 위로 한칸
    D: 아래로 한칸
"""
import sys 
input=sys.stdin.readline

N=int(input())
move_seq=list(input().split())

pos_x=1
pos_y=1
for move in move_seq:
    match move:
        case "L":
            if pos_y==1:
                continue
            else:
                pos_y-=1
        case "R":
            if pos_y==N:
                continue
            else:
                pos_y+=1
        case "U":
            if pos_x==1:
                continue
            else:
                pos_x-=1
        case "D":
            if pos_x==N:
                continue
            else:
                pos_x+=1
print(f"{pos_x} {pos_y}")
