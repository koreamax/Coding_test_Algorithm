import sys

input = sys.stdin.readline

N, M = map(int, input().split())
A = sorted([int(input()) for _ in range(N)]) # O(nlogn)

start, end = 0, 1 # 투 포인터
minimum = sys.maxsize # 최소 사이즈 

while (end < N):
    tmp = A[end] - A[start] # 현재 차
    
    if tmp < M: # 차가 M 보다 작으면 end를 늘려주기
        end += 1
    elif tmp > M: # 차가 M 보다 크면
        minimum = min(tmp, minimum) # 최솟값 비교
        if start == end: # start와 end가 같으면 end를 늘려주고
            end += 1
        else: # 아니라면 start만 추가
            start += 1
    else: # tmp == M
        minimum = M
        break

print(minimum)