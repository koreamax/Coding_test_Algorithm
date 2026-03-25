import sys

input = sys.stdin.readline

N = list(map(int, input().strip()))

# 버블정렬
for i in range(len(N)):
    isRight = True # 조기종료용 트리거
    for j in range(1, len(N) - i):
        if N[j-1] < N[j]:
            N[j-1], N[j] = N[j], N[j-1]
            isRight =  False
    if isRight: # true면 바뀐게 없으므로 조기종료
        break

print(*N, sep = '') # 공백없이 출력