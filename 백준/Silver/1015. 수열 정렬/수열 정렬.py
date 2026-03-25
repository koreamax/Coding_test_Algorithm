N = int(input())

A = list(map(int, input().split()))
B = sorted(A)
P = [0] * N

for i in range(N):
    for j in range(N):
        if A[i] == B[j]:
            P[i] = j
            B[j] = -1
            break

print(*P)