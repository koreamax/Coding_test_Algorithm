from sys import stdin

N, M = map(int, stdin.readline().split())

# 처음 가장 자리를 0으로 채워줌
li = [[0] for _ in range(N + 1)]
li[0] = [0 for _ in range(N + 1)]

# O(n^2) = 1000 * 1000
for i in range(1, N + 1):
    li[i] += (list(map(int, stdin.readline().split())))
    for j in range(1, N):
        li[i][j+1] += li[i][j] # y축 구간합 알고리즘

# O(n^2) = 1000 * 1000
for i in range(1, N):
    for j in range(1, N + 1):
        li[i+1][j] += li[i][j] # x축 구간합 알고리즘

# O(n) = 100000
for _ in range(M):
    x1, y1, x2, y2 = map(int, stdin.readline().split())
    # 2차원 구간합
    print(li[x2][y2] - li[x1-1][y2] - li[x2][y1-1] + li[x1-1][y1-1]) 