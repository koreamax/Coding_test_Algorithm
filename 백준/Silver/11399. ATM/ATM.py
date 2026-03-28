# 삽입정렬 연습해보기

import sys

input = sys.stdin.readline

N = int(input())
P = list(map(int, input().split()))
s = [0] * N
s[0] = P[0]

for i in range(1, N):
    valid = False
    for j in range(i-1, -1, -1):
        if P[i] > s[j]:
            valid = True
            break
    if valid:
        for k in range(len(s)-1, j+1, -1):
            s[k] = s[k-1]
        s[j+1] = P[i]
    else:
        for k in range(len(s)-1, -1, -1):
            s[k] = s[k-1]
        s[0] = P[i]

for i in range(N-1):
    s[i+1] += s[i]

print(sum(s))