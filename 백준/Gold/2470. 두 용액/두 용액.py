import sys

input = sys.stdin.readline

N = int(input())
l = sorted(list(map(int, input().split()))) # O(nlogn)

start, end = 0, N-1 # 투포인터
m = 10000000000 # 최솟값
arr = [0, 0] # 결과값 담기용

while(start != end):
    tmp = l[start] + l[end]
    if (tmp == 0): # 0이면 그냥 끝내버리기
        arr[0], arr[1] = l[start], l[end]
        break
    else: # 0이 아니면
        if (abs(tmp) < m): # 최소값 비교해서 작으면 바꿔주고
            arr[0], arr[1] = l[start], l[end]
            m = abs(tmp)
        
        if (tmp < 0): # 음수면 start를 더해서 양수로 만들고
            start += 1
        else: # 양수면 end를 빼서 음수로 만들기
            end -= 1

print(*arr)