import sys
from collections import deque

input = sys.stdin.readline

N, d, k, c = map(int, input().split())
f = []
window = deque() # 윈도우 사이즈용
dup = set() # 중복 검사용
cnt = [0] * d # 초밥 개수용
max = 0

# O(n) = 3,000,000
for _ in range(N):
    f.append(int(input())) # 초밥의 종류

# O(n) = 3,000,000 + 3,000
for i in range(N+k):
    # 윈도우에 값 추가
    window.append(f[i-N]) if i >= N else window.append(f[i])
    dup.add(window[-1]) # 중복검사 집합에도 추가
    cnt[window[-1] - 1] += 1 # 현재 윈도우 안의 초밥 개수
    if len(window) == k + 1:
        tmp = window.popleft() # 윈도우 안에 없는 초밥 제거
        cnt[tmp - 1] -= 1 # 현재 윈도우에서 빠져나가는 초밥 제거
        if not cnt[tmp - 1]: # 윈도우에 존재하지 않는다면
            dup.discard(tmp) # 옛날값 없애기
        dup.add(c) # 서비스 초밥 추가
        cnt[c - 1] += 1
        if len(dup) > max: # 최대값 바꿔주기
            max = len(dup)
        cnt[c - 1] -= 1
        if not cnt[c - 1]: # 해당 초밥이 없다면
            dup.discard(c) # 서비스 초밥 제거

print(max)