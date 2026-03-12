import sys

input = sys.stdin.readline

N , M = map(int, input().split())
arr = list(map(int, input().split()))
dp = 0 #dp는 더하고 끝낼거라 배열이 필요없음
remainder = [0 for _ in range(M)] # 나머지 값 저장

for i in range(N):
    dp += arr[i] # 구간 합 알고리즘
    remainder[dp % M] += 1 # 나머지 값에 1추가

cnt = remainder[0] # cnt는 구간의 합이 M으로 나눠지는 것들

for i in range(M):
    # 0과 1은 들어가면 안 되지만 어차피 0이 되기 때문에 들어감
    # nC2
    cnt += (remainder[i] * (remainder[i] - 1)) // 2

print(cnt)