import sys

input = sys.stdin.readline

N, S = map(int, input().split())
arr = list(map(int, input().split()))


start, end = 0, 0 # 투 포인터
m = N + 1 # 최소길이
sum = arr[0] # 윈도우 합

while (True): # end가 N까지 갔다는건 이제 끝이라는 것
    if (sum >= S): # sum이 더 크다면 길이 비교
        m = min(end - start + 1, m) # 길이가 최소값이라면 바꿔주기
        start += 1
        sum -= arr[start-1]
    else: # sum이 더 작으면 end를 더해주기
        end += 1
        if (end == N): # end가 끝까지 가면 끝
            break
        else:
            sum += arr[end]

print(m) if m != N+1 else print(0)