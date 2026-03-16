import sys
from collections import deque

input = sys.stdin.readline

N = int(input())

A = list(map(int, input().split()))
NGE = [0 for _ in range(N)]

d = deque()
d.append(0)

for i in range(1, N):
    while len(d) and A[d[-1]] < A[i]:
        NGE[d.pop()] = A[i]

    if i == N-1:
        NGE[i] = -1
        break
    else:
        d.append(i)

while len(d):
    NGE[d.pop()] = -1

print(*NGE)