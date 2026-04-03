"""
삽입 정렬
"""
arr=[7,5,9,0,3,1,6,2,4,8]

for i in range(1,len(arr)):
    for j in range(i,0,-1):
        if arr[j]<arr[j-1]:
            arr[j],arr[j-1]=arr[j-1],arr[j]
        else:
            break # 자기보다 작은 데이터를 만나면 그 위치에서 멈춤 -> 그 이전 요소들은 이미 정렬되어 있기 때문
print(arr)