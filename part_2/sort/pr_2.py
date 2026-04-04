"""
<< 성적이 낮은 순서로 학생 출력하기 >>
입력:
    첫번째 줄
        N: 학생 수
    두번째 줄
        학생이름 성적 
"""
import sys 
input=sys.stdin.readline

N=int(input().strip())
student={}
for _ in range(N):
    name,score=input().split()
    student[name]=int(score)

name_arr=sorted(student,key=student.get) # 각 key에 대해 value 기준으로 비교
print(name_arr)