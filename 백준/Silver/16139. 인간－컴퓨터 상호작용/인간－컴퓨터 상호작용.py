import sys

input = sys.stdin.readline

S = list(input().strip())
q = int(input())
# 알파벳마다 구간합 받을 수 있게 만들기
arr = [[0 for _ in range(len(S))] for _ in range(26)]

for i in range(26):
    for j in range(len(S)): # arr 채우기
        if ord(S[j]) == 97 + i:
            arr[i][j] = 1
    for j in range(len(S)-1): # 구간합 만들기
        arr[i][j+1] += arr[i][j]

for _ in range(q):
    alpha, l, r = input().split()
    n = ord(alpha) - 97
    l, r = int(l), int(r)
    print(arr[n][r]) if not l else print(arr[n][r] - arr[n][l-1])