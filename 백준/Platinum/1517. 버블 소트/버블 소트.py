import sys

input = sys.stdin.readline

N = int(input())
A = list(map(int, input().split()))
A = [[A[i]] for i in range(N)]

cnt = 0

while len(A) > 1:
    tmp = []
    for i in range(len(A) // 2):
        a = []
        idx_1, idx_2 = 0, 0 # 투 포인터
        while idx_1 != len(A[2*i]) and idx_2 != len(A[2*i+1]):
            if A[2*i][idx_1] < A[2*i+1][idx_2]:
                a.append(A[2*i][idx_1])
                idx_1 += 1
            elif A[2*i][idx_1] > A[2*i+1][idx_2]:
                a.append(A[2*i+1][idx_2])
                cnt += len(A[2*i])-idx_1
                idx_2 += 1
            else:
                a.append(A[2*i][idx_1])
                idx_1 += 1
        if idx_1 == len(A[2*i]):
            while(idx_2 != len(A[2*i+1])):
                a.append(A[2*i+1][idx_2])
                idx_2 += 1
        else:
            while(idx_1 != len(A[2*i])):
                a.append(A[2*i][idx_1])
                idx_1 += 1
        tmp.append(a)
    if len(A) % 2 == 1:
        A = tmp + [A[-1]]
    else:
        A = tmp

print(cnt)