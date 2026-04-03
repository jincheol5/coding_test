"""
<< 왕실의 나이트 (p.115) >>
    8 X 8 보드 
    행: 1~8
    열: a~h
    힌트:
        아스키코드값 확인 함수: ord
"""
import sys
input=sys.stdin.readline

knight_pos=input()

### 좌표 계산
pos_init_x=ord("a")
pos_x=ord(knight_pos[0])-pos_init_x+1
pos_y=int(knight_pos[1])

### 경우의 수 계산
# total=0
# if pos_x-2>=1:
#     if pos_y-1>=1:
#         total+=1
#     if pos_y+1<=8:
#         total+=1
# if pos_x+2<=8:
#     if pos_y-1>=1:
#         total+=1
#     if pos_y+1<=8:
#         total+=1
# if pos_y-2>=1:
#     if pos_x-1>=1:
#         total+=1
#     if pos_x+1<=8:
#         total+=1
# if pos_y+2<=8:
#     if pos_x-1>=1:
#         total+=1
#     if pos_x+1<=8:
#         total+=1
# print(total)


### 정답 코드
steps=[(2,1),(2,-1),(1,2),(-1,2),(-2,1),(-2,-1),(1,-2),(-1,-2)]

valid_step=0
for step in steps:
    next_x_pos=pos_x+step[0]
    next_y_pos=pos_y+step[1]
    if next_x_pos>=1 and next_x_pos<=8 and next_y_pos>=1 and next_y_pos<=8:
        valid_step+=1
print(valid_step)