"""
<< 게임 개발 (p.118) >>
입력값:
    첫째줄
        N: 맵의 세로 크기
        M: 맵의 가로 크기
    둘째줄
        캐릭터 좌표, 방향 (0:북,1:동,2:남,3:서)
    셋째줄
        맵 정보 (0:육지,1:바다)
"""
import sys
input=sys.stdin.readline

N,M=map(int,input().split())
pos_x,pos_y,direction=map(int,input().split())
map_info=[list(map(int,input().split())) for _ in range(N)]

direction_dict={
    0:(0,-1),
    1:(0,1),
    2:(-1,0),
    3:(1,0)
}

visited_set=set()
visited_set.add((pos_x,pos_y))

visited_count=1
all_direction_count=0
while True:
    # 방향 지정
    direction-=1
    if direction==-1:
        direction=3
    
    # 이동 여부 확인
    next_pos_x=pos_x+direction_dict[direction][0]
    next_pos_y=pos_y+direction_dict[direction][1]
    if map_info[next_pos_x][next_pos_y]==0 and (next_pos_x,next_pos_y) not in visited_set:
        visited_set.add((next_pos_x,next_pos_y))
        pos_x=next_pos_x
        pos_y=next_pos_y
        visited_count+=1
    else:
        all_direction_count+=1
        if all_direction_count==4:
            # 한칸 뒤로
            pos_x=pos_x-direction_dict[direction][0]
            pos_y=pos_y-direction_dict[direction][1]
            all_direction_count=0
            if map_info[pos_x][pos_y]==1:
                break
print(visited_count)