import sys

input = sys.stdin.readline

N, M = map(int, input().split())
arr = list(map(int, input().split()))

# O(n) = 100000
for i in range(1, N): # 구간합 만들기
    arr[i] += arr[i-1]
# O(n) = 100000
for _ in range(M):
    i ,j = map(int, input().split())
    # i는 -2를 해줘야 하므로 조건 넣기
    print(arr[j-1]) if i == 1 else print(arr[j-1] - arr[i-2])