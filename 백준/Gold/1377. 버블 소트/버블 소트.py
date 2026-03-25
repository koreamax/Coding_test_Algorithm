import sys

input = sys.stdin.readline
# 왼쪽 인덱스 바뀐 만큼의 최대값을 구하면 됨
N = int(input())
A = [(int(input()), i) for i in range(N)]
B = sorted(A) # O(nlogn) = 500,000 * (5 + ...)
M = 0

# O(n) = 500,000
for i in range(N):
    M = max(B[i][1] - i, M)

print(M+1)