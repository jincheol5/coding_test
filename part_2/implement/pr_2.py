"""
<< 시각 (p.113) >>
"""
import sys
input=sys.stdin.readline

N=int(input())

# 3 13 23 30~39 43 53 
total=0
for t in range(N+1):
    for minute in range(60):
        for second in range(60):
            if "3" in str(t)+str(minute)+str(second):
                total+=1
print(total)

