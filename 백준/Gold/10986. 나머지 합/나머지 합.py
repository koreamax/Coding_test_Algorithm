import sys

input = sys.stdin.readline

N , M = map(int, input().split())
arr = list(map(int, input().split()))
cnt = 0 # M으로 나누어 떨어지는 구간의 개수
dp = [arr[0]]
remainder = [0 for _ in range(M)]
remainder[dp[-1] % M] += 1

# 부분 합 알고리즘, O(n) = 1000000
for i in range(N-1):
    # (a + b) % c = ((a % c) + (b % c)) % c -> 메모리 용량 줄이기
    dp.append(((arr[i+1] % M) + (dp[i] % M)) % M)
    remainder[dp[-1] % M] += 1

# 나머지가 0인 것들
cnt += remainder[0]

# O(n) = 1000
for i in range(M):
    if remainder[i] >= 2:
        cnt += (remainder[i] * (remainder[i] - 1)) // 2

print(cnt)