import sys

input = sys.stdin.readline

S = list(input().strip())
q = int(input())
# 알파벳마다 구간합 받을 수 있게 만들기
arr = [[0]*(len(S)+1) for _ in range(26)]

for i in range(26):
    for j in range(len(S)): # 구간합 만들기
        arr[i][j+1] += arr[i][j]
        if ord(S[j]) == 97 + i:
            arr[i][j+1] += 1

for _ in range(q):
    alpha, l, r = input().split()
    print(arr[ord(alpha) - 97][int(r)+1] - arr[ord(alpha) - 97][int(l)])